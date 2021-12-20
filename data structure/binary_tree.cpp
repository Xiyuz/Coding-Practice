//Binary tree: each node has at most two children
//This file implements an increasing order binary search tree
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;
struct Node
{
    int data;
    Node* left_child;
    Node* right_child;
    Node(int val)
    {
        data = val;
        left_child = NULL;
        right_child = NULL;
    }
};

Node* search();
int main()
{
    Node temp = Node(10);
    cout<<temp.data;
    return 0;
}