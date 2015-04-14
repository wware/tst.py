// C program to demonstrate Ternary Search Tree (TST) insert, travese
// and search operations
#include <stdio.h>
#include <stdlib.h>
#define MAX 50

// A node of ternary search tree
struct Node
{
    char data;

    // True if this character is last character of one of the words
    unsigned isEndOfString: 1;

    struct Node *left, *eq, *right;
};

// We only ever need a single root, but if we ever want to change to a
// new tree, we'll need a way to deallocate everything and clean up.
static struct Node* root = NULL;

static void cleanup_helper(struct Node *node)
{
    if (node) {
        cleanup_helper(node->left);
        cleanup_helper(node->eq);
        cleanup_helper(node->right);
        free(node);
    }
}

void cleanup(void)
{
    cleanup_helper(root);
    root = NULL;
}

// A utility function to create a new ternary search tree node
static struct Node* newNode(char data)
{
    struct Node* temp = (struct Node*) malloc(sizeof( struct Node ));
    temp->data = data;
    temp->isEndOfString = 0;
    temp->left = temp->eq = temp->right = NULL;
    return temp;
}

static void insert_helper(struct Node **root, char *word)
{
    // Base Case: Tree is empty
    if (!(*root))
        *root = newNode(*word);

    // If current character of word is smaller than root's character,
    // then insert this word in left subtree of root
    if ((*word) < (*root)->data)
        insert_helper(&( (*root)->left ), word);

    // If current character of word is greate than root's character,
    // then insert this word in right subtree of root
    else if ((*word) > (*root)->data)
        insert_helper(&( (*root)->right ), word);

    // If current character of word is same as root's character,
    else
    {
        if (*(word+1))
            insert_helper(&( (*root)->eq ), word+1);

        // the last character of the word
        else
            (*root)->isEndOfString = 1;
    }
}

// Function to insert a new word in a Ternary Search Tree
void insert(char *word)
{
    insert_helper(&root, word);
}

// A recursive function to traverse Ternary Search Tree
static void traverseTSTUtil(struct Node *root, char* buffer, int depth)
{
    if (root)
    {
        // First traverse the left subtree
        traverseTSTUtil(root->left, buffer, depth);

        // Store the character of this node
        buffer[depth] = root->data;
        if (root->isEndOfString)
        {
            buffer[depth+1] = '\0';
            printf( "%s\n", buffer);
        }

        // Traverse the subtree using equal pointer (middle subtree)
        traverseTSTUtil(root->eq, buffer, depth + 1);

        // Finally Traverse the right subtree
        traverseTSTUtil(root->right, buffer, depth);
    }
}

// The main function to traverse a Ternary Search Tree.
// It mainly uses traverseTSTUtil()
void traverse(void)
{
    char buffer[MAX];
    traverseTSTUtil(root, buffer, 0);
}

// Function to search a given word in TST
int search_helper(struct Node *root, char *word)
{
    if (!root)
        return 0;

    if (*word < root->data)
        return search_helper(root->left, word);

    else if (*word > root->data)
        return search_helper(root->right, word);

    else
    {
        // words end on anything that isn't a letter
        char c = *(word + 1);
        if (c < 'A' || (c > 'Z' && c < 'a') || c > 'z')
            return root->isEndOfString;

        return search_helper(root->eq, word+1);
    }
}

// Function to search a given word in TST
int search(char *word)
{
    return search_helper(root, word);
}

#ifndef LIB
// Driver program to test above functions
int main()
{
    insert("cat");
    insert("cats");
    insert("up");
    insert("bug");

    printf("Following is traversal of ternary search tree\n");
    traverse();

    printf("\nFollowing are search results for cats, bu and cat respectively\n");
    search("cats")? printf("Found\n"): printf("Not Found\n");
    search("bu")?   printf("Found\n"): printf("Not Found\n");
    search("cat")?  printf("Found\n"): printf("Not Found\n");

    return 0;
}
#endif
