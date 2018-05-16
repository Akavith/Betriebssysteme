package studentLock;

import java.util.List;

public class Student implements Runnable {
	
	private int readingTime;
	private String name;
	private int counts = 0;
	private boolean isHavingBooks = false;
	private List<Book> BookList1;
	private List<Book> BookList2;
	private List<Book> BookList3;
	private Book book1 = null;
	private Book book2 = null;
	private Book book3 = null;
	
	
	public Student(String name, int readingTime, List<Book> l1, List<Book> l2, List<Book> l3) {
		this.readingTime = readingTime;
		this.BookList1 = l1;
		this.BookList2 = l2;
		this.BookList3 = l3;
		this.name = name;
	}
	
	public String getName() {
		return name;
	}


	public int getCounts() {
		return counts;
	}




	public boolean isHavingBooks() {
		return isHavingBooks;
	}




	@Override
	public void run() {
		
		while(true) {
			if(book1 == null) {
				synchronized(BookList1) {
					if(!BookList1.isEmpty()) {
						book1 = BookList1.remove(0);
					}
				}
			}
			
			if(book2 == null) {
				synchronized(BookList2) {
					if(!BookList2.isEmpty()) {
						book2 = BookList2.remove(0);
					}
				}
			}
			
			if(book3 == null) {
				synchronized(BookList3) {
					if(!BookList3.isEmpty()) {
						book3 = BookList3.remove(0);
					}
				}
			}
			
			if(!(book1 == null || book2 == null || book3 == null)) {
				try {
					isHavingBooks = true;
					counts++;
					Thread.sleep(readingTime);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			
			if(book1 != null) {
				synchronized(BookList1) {
					BookList1.add(book1);
				}
				book1 = null;
				isHavingBooks = false;
			}
				
			if(book2 != null) {
				synchronized(BookList2) {
					BookList2.add(book2);
				}
				book2 = null;
				isHavingBooks = false;
			}
				
			if(book3 != null) {
				synchronized(BookList3) {
					BookList3.add(book3);
				}
					book3 = null;
					isHavingBooks = false;
			}
		}
	
	}
	

}
