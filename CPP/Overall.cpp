/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//DATA TYPES
//VECTOR
//making a 2d vector
vector<vector<bool>> dp(n,vector<bool>(n,false)); // vector of size n,n with false as default value

//ADDING ITEM IN FRONT OF VECTOR
vector<int> ans;
ans.insert(vector.begin(),100);

//STACK
stack<int> comp; // creating a stack
stack.push(10); // push elem in the stack
int top = stack.top(); // view the top element
stack.pop(); // no return value

//TREES
root->left; // to get left child
root->right; //to get right child
root->value; // to get the value

/////////////////////////////////////////////////////////////////
//STRING
//SUB-STRING
string r = s1.substr(1, 3); // 3 CHARACTERS FROM POS 1



/////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DATA TYPE CONVERSIONS

//INT TO STRING
int x = 10;
auto revs = std::to_string(x);
reverse(revs.begin(), revs.end());

//STRING TO INT
string temp;
int ans = stoi(temp);

////////////////////////////////////////////////////////////////////////////////////////////////////////////
// ACCESSING
//READING A CHARACTER OF STRING
char compare = strs.at(x);


////////////////////////////////////////////////////////////////////////////////////////////////////////////
//binary search
//fstart and fend are 2 different vectors

int starttime = upper_bound(fstart.begin(),fstart.end(),it) - fstart.begin(); //bisect_right
int endtime = lower_bound(fend.begin(),fend.end(),it) - fend.begin(); // bisect_left

//
