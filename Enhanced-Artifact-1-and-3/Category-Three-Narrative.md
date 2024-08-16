# Category Three Narrative: Databases

## Briefly describe the artifact. What is it? When was it created?

This artifact is a course catalog application adapted from a project I completed in CS-300: Data Structures & Algorithms course last fall. It also blends elements of a full stack application I created during a course in CS-340: Client-Server Architecture. The original project from CS-300 was a simple C++ console app that only gave users the ability to search for a course or print courses in alphanumeric order. This new version has a fully functional web interface that allows users to search for courses, explore the catalog, and even register and deregister from courses.

## Justify the inclusion of the artifact in your ePortfolio. 
This artifact serves as my enhancement for categories one and three. As I’ve already completed my narrative for category one, I will focus on this artifact’s inclusion as it relates to category three. The original program stored the courses in a binary search tree, but I chose to implement this new solution using MongoDB and an HTML interface. I went through the process of loading the dataset into MongoDB and then writing a Python module that would handle calls to the database. This module is then invoked in the main application code in order to display the course catalog and retrieve course information. Additionally, I created a second database for students that allows unique student users to create accounts in order to register or deregister for classes by keeping an array of student IDs associated with each course in the catalog. This artifact demonstrates my ability to effectively use MongoDB to create solutions with multiple databases, all while providing a simple, intuitive interface for users.


## Did you meet the course objectives you planned to meet with this enhancement in Module One? 


## Reflect on the process of enhancing and modifying the artifact. 
