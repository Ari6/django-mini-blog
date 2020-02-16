# django-mini-blog
Mini blog 

## Models
* User
	* Bio(char)
* Post
	* Title(char)
	* Post date(date)
	* Content(char)
	* Author/User
	* Public(boolean)
* Comment
	* Post
	* Comment date(date)
	* Comment(char)
	* Author/User

## Pages
* / and /blog/
	* Index
* /blog/blogs/
	* accessible to all users from a sidebar link
	* Sorted by post date(neweest to oldest)
	* Paginated 5 articles
	* Show title, post date and author
	* Blog title are linked to blog detail pages.
	* Author are linked to blog author detail pages.
* /blog/blogger/<author-id>
	* accessible to all users from author links in blog posts, etc.
	* Contains some bio information.
	* Sorted by post date (newest to oldest)
	* No paginated.
	* Shows blog title and post date.
* /blog/<blog-id>
	* blog details
	* accessible to all users from blog post lists
	* Contains title, author, post date, and content.
* /blog/bloggers/
	* accessible to all users from site sidebar
	* Blogger names are linked to Author detail pages
* /blog/<blog-id>/create
	* create comment for blog post.
	* accessible to logged-in users from link at bottom of blog post detail pages.
	* Displays form with description for entering comments.
	* After a comment has been posted, the page will redirect back to the associated blog post page.
	* Users cannot edit or delte their posts.
	* Lgged out users will be directed to the login page, before they can add comments. After logging in, they will be redirected back to the blog page they wanted to comment on.
	* Comment pages should include the name link to the blogpost being commented on.
* /accounts/<standardurls>
		* Login/logout should be accessiblle via sidebar links.
* /admin/<standardurls>
		* Admin site blog posts records should display the list of associated comments inline.
		* Comment names in the Admin site are created by truncating the comment description to 75 characters.
		* Other types of records can use basic registration.
