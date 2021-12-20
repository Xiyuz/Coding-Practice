#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;
#define MAX 1000
class Stack
{
    private:
        int top;
    public:
        int a[MAX];//max size of the Stack
        Stack();
        bool push(int x);
        int pop();
        int peek();
        bool isEmpty();
};

Stack::Stack()
{
    top = -1;
}

bool Stack::push(int x)
{
    if (top == MAX - 1)
    {
        cout<<"Stack Overflow"<<endl;
        return false;
    }

    top++;
    a[top] = x;
    cout<<x<<" is pushed on Stack"<<endl;
    return true;
}

int Stack::pop()
{
    if (top < 0)
    {
        cout<<"Stack Underflow"<<endl;
        return 1;
    }
    return a[top--];

}

int Stack::peek()
{
    if (top < 0)
    {
        cout<<"Stack Underflow"<<endl;
        return 1;
    }
    return a[top];
}

bool Stack::isEmpty()
{
    return (top < 0);
}

int main()
{
    Stack stack = Stack();
    stack.peek();
    stack.push(3);
    cout<<stack.pop()<<endl;
}