/*
	Title:  LinkedList.h
	Author: Jevin Evans
	Date:  3/19/2018
	Purpose: Singly- LinkedList for Program 6
*/
#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <cstddef>
#include <iostream>
using namespace std;

template<typename Type> 
class LinkedList
{
	private:
		struct ListNode
		{
			Type value;
			struct ListNode *next;
		};
		
		ListNode* head;
		ListNode* tail;
		int numNodes;

		//Index is 1 based not 0 based
		
		ListNode* getNode(int position)
			{
				ListNode* node;
				 if(position == 1)
					return head;
				
				else if(position <= numNodes)
				{
					node = head;
					
					int current = 1;
					
					while(position >= current)
					{
						if(position == current)
							return node;
						 
						current++;
						node = node->next;
					}
				}
			}
	public:
			LinkedList()
			{
				head = NULL;
				tail = NULL;
				numNodes = 0;
			}
		
			~LinkedList() //THis needs work
			{
				// cout << "Starting List Deletion...";
				ListNode* delNode, *next;
				
				delNode = head;
				while(this->numNodes != 0)
				{					
					next = delNode->next; 
					// delNode->value->PRINT();
					// cout << endl;
					delete delNode;
					--this->numNodes;
					delNode = next;
				}
				delete head, tail;
				// cout << "LinkedList Deleted" << endl;
			}
			
			int getLength()
			{
				return numNodes; 				
			}
				
			Type getNodeValue(int position)
			{
				ListNode* node = new ListNode;
				 if(position == 1)
					return head->value;
				
				else if(position <= numNodes)
				{
					node = head;
					
					int current = 1;
					
					while(position >= current)
					{
						if(position == current)
							return node->value;
						 
						current++;
						node = node->next;
					}
				}
				return NULL;
			}
						
			void appendNode(Type object)
			{
				ListNode* node = new ListNode;
				node->value = object;
				node->next = NULL;
				
				if(!head)
				{
					head = node;
					tail = node;
					numNodes++;
				}
				else
				{
						tail->next = node;
						tail = node;
						numNodes++;
				}
			}
			
			void deleteNode(int position)
			{
				
				ListNode* now = new ListNode;
				ListNode* prev = new ListNode;
				
				if(!head)
					return;
				
				if(position == 1)
				{
					now = head;
					head = head->next;
					delete now;
					numNodes--;
				}
				else
				{
					now = head;
					int cur = 1;
					
					while(cur <= position)
					{
						cout << "Deleting: " << now->value << endl;
						if(position == numNodes)
						{
							tail = prev;
						}
						if(position == cur)
						{
							prev->next = now->next;
							delete now;
							numNodes--;
						}
						cur++;
						prev = now;
						now = now->next;
					}
				}
				
			}

			void display()
			{
				ListNode* tmp = new ListNode();
				tmp = head;
				
				while(tmp)
				{
					cout << tmp->value << "\t";
					tmp = tmp->next;
				}

			}

			void swap(int num1, int num2)
			{
				ListNode* node1 = getNode(num1);
				ListNode* node2 = getNode(num2);
				
				Type temp;
				temp = node1->value;
				node1->value = node2->value;
				node2->value = temp;
			}		
};
#endif