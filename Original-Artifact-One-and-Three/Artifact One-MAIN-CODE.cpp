//====================================================
// Name: Project Two CS300.cpp
// Author: Max Pinson
// Version: 1
// Description: Program for course management at ABCU
//====================================================
# include <iostream>
# include <vector>
# include <string>
# include <fstream>
# include <sstream>
# include <cstring>

using namespace std;
//========================
//   Global definitions
//========================

// structure holds course information
struct Course {
	string courseNum;
	string courseId;
	string name;
	vector<string> prerequisites;

	Course() {
		courseId = "null";
		name = "null";
		prerequisites = {};
	}
};

// binary search tree node object
struct Node {
	Course course;
	Node* left;
	Node* right;

	Node() { // default constructor
		left = nullptr;
		right = nullptr;
	}

	Node(Course course1) : // initializes with a bid
		Node() {
		course = course1;
	}
};

//==============================================
//    Binary Search Tree Class Definition
//==============================================
class BinarySearchTree {

private:
	Node* root;
	void addNode(Node* node, Course course);
	void inOrder(Node* node);
	void prereqCheck(Node* node);

public:
	BinarySearchTree();
	virtual ~BinarySearchTree();
	void Destroy(Node* node);
	void InOrder();
	void Insert(Course course);
	void Print(Node* node);
	void PrereqCheck();
	Course Search(string courseId);
	int size;
};

/**
* Default constructor
*/
BinarySearchTree::BinarySearchTree() {
	root = nullptr;
	size = 0;
}

/**
* Destructor
*/
BinarySearchTree::~BinarySearchTree() {
	Destroy(root);
}

/**
* Recursive node destruction to support tree destruction
*/
void BinarySearchTree::Destroy(Node* node) {
	if (node != nullptr) {
		if (node->right == nullptr && node->left == nullptr) {
			delete node;
			node = nullptr;
		}
		else {
			Destroy(node->right);
			Destroy(node->left);
		}
	}
	return;
}

/**
* Public function to traverse tree in order
*/
void BinarySearchTree::InOrder() {
	inOrder(root);
}

/**
* Insert a node that holds a course object into the tree
*/
void BinarySearchTree::Insert(Course course) {
	Node* node = new Node(course);

	if (root == nullptr) {
		root = node;
	}
	else {
		this->addNode(root, course);
	}
}

/**
* Search for a course by Id
*/
Course BinarySearchTree::Search(string courseId) {
	Course course;
	Node* currNode = root;

	while (currNode != nullptr) {
		if (currNode->course.courseId == courseId) { // found match
			return currNode->course;
		}
		else if (currNode->course.courseId < courseId) { // traverse right branch
			currNode = currNode->right;
		}
		else if (currNode->course.courseId > courseId) { // traverse left branch
			currNode = currNode->left;
		}
	}
	return course;
}

/**
* Adds node to Binary Search Tree
*
* @param node current node in tree (pass root to add to correct position in tree)
* @param course course object to be added
*/
void BinarySearchTree::addNode(Node* node, Course course) {
	if (node != nullptr && node->course.courseId.compare(course.courseId) > 0) {
		if (node->left == nullptr) { // finds node with no left child
			node->left = new Node(course);
			return;
		}
		else {
			this->addNode(node->left, course); // recursively traverses tree to the left
		}
	}

	else if (node != nullptr && node->course.courseId.compare(course.courseId) < 0) {
		if (node->right == nullptr) { // finds node with no right child
			node->right = new Node(course);
		}
		else {
			this->addNode(node->right, course); // recursively traverses tree to the right
		}
	}
}
/**
* Prints course list in alphanumeric order
*/
void BinarySearchTree::inOrder(Node* node) {
	if (node != nullptr) {
		inOrder(node->left);
		Print(node);
		inOrder(node->right);
	}
}

/**
* Public method to verify prerequisites
*/
void BinarySearchTree::PrereqCheck() {
	prereqCheck(root);
}

/**
* Verifies that all prerequisites are also courses
* @param node current node (pass root to check whole tree)
*/
void BinarySearchTree::prereqCheck(Node* node) {
	if (node != nullptr) {
		prereqCheck(node->left); // recursively checks all nodes
		for (unsigned int i = 0; i < node->course.prerequisites.size(); ++i) {
			if (Search(node->course.prerequisites.at(i)).courseId == "null") { // prerequisite does not match any existing courses
				cout << "Invalid prerequisite: " << node->course.prerequisites.at(i) << endl;
				node->course.prerequisites.erase(node->course.prerequisites.begin() + i); // deletes invalid prerequisites
				i -= 1; // ensures that after removing a prerequisite, no course is skipped
			}
		}
		prereqCheck(node->right);
	}
}

/**
* Prints the details of the course object associated with a given node
*/
void BinarySearchTree::Print(Node* node) {
	cout << node->course.courseId << " | " << node->course.name << " | " << "Prerequisites: ";
	if (node->course.prerequisites.size() == 0) { // accounts for courses with no prerequisites
		cout << "none" << endl;
	}
	else { // iterate through prerequisite vector
		for (unsigned int i = 0; i < node->course.prerequisites.size(); ++i) {
			if (i == node->course.prerequisites.size() - 1) {
				cout << node->course.prerequisites.at(i) << endl;
			}
			else {
				cout << node->course.prerequisites.at(i) << ", ";
			}
		}
	}
}

//==================================================================================================================

vector<Course> courses; // vector for global use in main

/**
* Prints course info
*/
void displayCourse(Course course) {
	cout << course.courseId << " | " << course.name << " | " << "Prerequisites: ";
	if (course.prerequisites.size() == 0) {
		cout << "none" << endl;
	}
	else {
		for (unsigned int i = 0; i < course.prerequisites.size(); ++i) {
			if (i == course.prerequisites.size() - 1) {
				cout << course.prerequisites.at(i) << endl;
			}
			else {
				cout << course.prerequisites.at(i) << ", ";
			}
		}
	}

	return;
}

/**
* Finds highest number of prerequisites associated with a single course
*/
int maxNumPrereqs(vector<Course> courses) {
	int max = 0;
	for (unsigned int i = 0; i < courses.size(); ++i) {
		if (courses.at(i).prerequisites.size() > max) {
			max = courses.at(i).prerequisites.size();
		}
	}
	return max;
}

/**
* Determines if all of a courses prerequisites have been printed in the PrintInOrder() function
*
* @param courses vector that holds unprinted courses
* @param prereqs vector that holds prereqs for a given course
*/
bool AlreadyPrinted(vector<Course> courses, vector<string> prereqs) {
	for (unsigned int i = 0; i < courses.size(); ++i) {
		for (unsigned int j = 0; j < prereqs.size(); ++j) {
			if (courses.at(i).courseId == prereqs.at(j)) { // course has prereq that has not been printed yet
				return false;
			}
		}
	}
	return true;
}

/**
* Prints courses in order that obeys prerequisite requirements
*/
void PrintInOrder() {
	int coursesPrinted = 0;
	int updatedSize = 0;
	vector<Course>coursesNew = courses; // copies courses vector
	int numCourses = courses.size();

	cout << "Sample Schedule:" << endl;

	// iterates until all courses have been printed or for loops have iterated without printing any new courses
	while (coursesPrinted != numCourses && coursesNew.size() != updatedSize) {
		updatedSize = coursesNew.size(); // tracks vector size before for loops
		for (unsigned int j = 0; j < maxNumPrereqs(courses) + 1; ++j) {
			for (unsigned int i = 0; i < coursesNew.size(); ++i) {
				// if course has a specific number of prerequisites and they've already been printed
				if (coursesNew.at(i).prerequisites.size() == j && AlreadyPrinted(coursesNew, coursesNew.at(i).prerequisites)) {
					displayCourse(coursesNew.at(i));
					coursesNew.erase(coursesNew.begin() + i); // erase printed course to signify it has been printed
					coursesPrinted += 1; // increment count of courses already printed
				}
			}
		}
	}
	cout << endl;
	if (coursesPrinted != numCourses) { // while loop exited without printing all courses
		cout << "Impossible schedule. Following courses cannot be scheduled:" << endl;
		for (unsigned int i = 0; i < coursesNew.size(); ++i) { // shows remaining courses causing prerequisite logic errors
			displayCourse(coursesNew.at(i));
		}
	}
}

/**
* Loads courses from file into binary search tree.
* Returns size of bst upon completion of file read.
*
* @params filePath file from which to load data
* @params bst Binary Search Tree into which to load data
*/
int loadCourses(string filePath, BinarySearchTree* bst) {
	ifstream inFS;
	vector<string> row;
	string line = "line";
	string word, temp;

	cout << "Opening " << filePath << endl;
	inFS.open(filePath);

	if (!inFS.is_open()) { // displays error and exits if file does not open
		cout << "Error. Could not open file" << endl;
		return 1;
	}

	while (getline(inFS, line)) { // loops until empty line

		row.clear(); // clears previous row

		// parses line into string values separated by commas
		stringstream s(line);
		while (getline(s, word, ',')) {
			row.push_back(word);
		}

		Course course; // instantiate new object
		try {
			course.courseId = row.at(0); // assigns courseId with first value
			course.name = row.at(1); // assigns course name with second value

			for (unsigned int i = 2; i < row.size(); ++i) { // adds all remaining values to prerequisite vector
				course.prerequisites.push_back(row.at(i));
			}

			bst->Insert(course);
			courses.push_back(course);

			bst->size += 1; // increments number of nodes in bst
		}

		catch (const out_of_range& e) { // if row has fewer than two values
			cout << "Please ensure that all courses have ID and name" << endl;
		}
	}

	bst->PrereqCheck(); // verifies validity of all prerequisites

	inFS.close();

	return bst->size;
}

int main(int argc, char* argv[]) {

	string filePath;
	switch (argc) {
	case 2:
		filePath = argv[1];
		break;
	default:
		filePath = "CourseList.txt";
	}

	// Define a binary search tree to hold all bids
	BinarySearchTree* bst;
	bst = new BinarySearchTree();
	Course course;
	string courseId;

	int choice = 0;
	while (choice != 9) { // displays menu until user presses exit key
		cout << "Menu:" << endl;
		cout << "  1. Load Courses" << endl;
		cout << "  2. Display Courses in Alphanumeric Order" << endl;
		cout << "  3. Find Course" << endl;
		cout << "  4. Display Courses in Order Obeying Prerequisites" << endl;
		cout << "  9. Exit" << endl;
		cout << "Enter choice: ";
		cin >> choice;

		switch (choice) {

		case 1: // loads courses from file into Binary Search Tree
			cout << endl;
			cout << loadCourses(filePath, bst) << " courses read" << endl;
			cout << endl;
			break;

		case 2: // prints courses in alphanumeric order
			cout << endl;
			bst->InOrder();
			cout << endl;
			break;

		case 3: // gets user input courseId and searches tree for it
			cout << endl;
			cout << "Enter course to search for" << endl;
			cin >> courseId;
			cout << endl;

			for (unsigned int i = 0; i < courseId.length(); ++i) {
				courseId.at(i) = toupper(courseId.at(i));
			}

			course = bst->Search(courseId);

			if (course.courseId != "null") {
				displayCourse(course);
				cout << endl;
			}
			else { // prints error message if course not found
				cout << "Course Id " << courseId << " not found." << endl;
				cout << endl;
			}

			break;

		case 4: // prints in order obeying prerequisites
			cout << endl;
			PrintInOrder();
			cout << endl;
			break;
		}
	}
	cout << "Good bye." << endl;

	return 0;
}


