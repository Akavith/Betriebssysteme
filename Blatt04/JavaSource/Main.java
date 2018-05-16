package studentLock;

import java.util.ArrayList;
import java.util.List;

public class Main {
	
	@SuppressWarnings("serial")
	public static void main(String... args) {
		
		List<Book> BookList1 = new ArrayList<Book>();
		List<Book> BookList2 = new ArrayList<Book>();
		List<Book> BookList3 = new ArrayList<Book>();
		
		BookList1.add(new Book());
		BookList1.add(new Book());
		BookList1.add(new Book());
		
		BookList2.add(new Book());
		BookList2.add(new Book());
		
		BookList3.add(new Book());
		BookList3.add(new Book());
		
		
		List<Student> students = new ArrayList<Student>();
		
		for(int i = 0; i < Integer.valueOf(args[0]);i++) {
			Student s = new Student("Student" + i,Integer.valueOf(args[1]),BookList1, BookList2, BookList3);
			students.add(s);
			(new Thread(s)).start();
		}
		
		
		while(true) {
			
			System.out.println("Studentenausleihe:");
			
			int studentsHavingBooks = 0;
			for(Student s : students) {
				System.out.println(s.getName() + " had all Books " + s.getCounts() + " times.");
				if(s.isHavingBooks()) {
					studentsHavingBooks++;
				}
			}
			System.out.println(studentsHavingBooks + "Students currently have all BookS\n");
			
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

}
