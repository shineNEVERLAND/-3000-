#include<stdio.h>
#include<iostream>
#include<map>
#include<unordered_map>
#include<vector>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int> >& board) {
         if (board.size() == 0)
            return ;
        int rowLength = board.size();
        int columnLength = board[0].size();
        unordered_map<int, int> modify_zero;
        unordered_map<int, int> modify_one;
        for(int i = 0;i < rowLength;++i)
        {
            for(int j = 0; j < columnLength; ++j)
            {
                int num = 0;
                if(i - 1 >= 0 && j - 1 >= 0 && board[i-1][j-1] == 1)
                    num++;
                if(i - 1 >= 0 && board[i-1][j] == 1)
                    num++;
                if(i - 1 >= 0 && j + 1 < columnLength && board[i-1][j+1] == 1)
                    num++;
                if(j - 1 >= 0 && board[i][j-1] == 1)
                    num++;
                if(j + 1 < columnLength && board[i][j+1] == 1)
                    num++;
                if(i + 1 < rowLength && j - 1 >= 0 && board[i+1][j-1] == 1)
                    num++;
                if(i + 1 < rowLength && board[i+1][j] == 1)
                    num++;
                if(i + 1 < rowLength && j + 1 < columnLength && board[i+1][j+1] == 1)
                    num++;
                
                if(num < 2 || num > 3)
                    modify_zero.insert(pair<int, int>(i, j));
                else if(board[i][j] == 0 && num == 3)
                    modify_one.insert(pair<int, int>(i, j));
            }
        }
        unordered_map<int, int>::iterator it = modify_zero.begin();
        while(it != modify_zero.end())
        {
            board[it->first][it->second] = 0;
            it++;
        }
        unordered_map<int, int>::iterator it2 = modify_one.begin();
        while(it2 != modify_one.end())
        {
            board[it2->first][it2->second] = 1;
            it2++;
        }
        
    }
};

int
main()
{
    vector<int> item;
    item.push_back(1);
    item.push_back(1);
    vector<vector<int> > board;
    board.push_back(item);
    Solution A = Solution();
    A.gameOfLife(board);
    printf("Hello World\nWelcome to go to C++\n");
}