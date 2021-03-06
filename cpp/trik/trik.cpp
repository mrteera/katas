/* http://programming.in.th/task/rev2_problem.php?pid=0010 */
#define CATCH_CONFIG_MAIN
#include "../catch.hpp"
#include <string>
#include <iostream>
using namespace std;

/*
 * TODO:
 * - Refactor to use switch case
 * - Use class
*/


int Trik( char cipher[50] ) {
    int ball_position_1 = 1;
    int ball_position_2 = 0;
    int ball_position_3 = 0;
    int ball_position_temp;

    char* index = cipher;
    for (; *index != '\0'; ++index) {
        if ( *index == 'A' ) {
            ball_position_temp = ball_position_2;
            ball_position_2 = ball_position_1;
            ball_position_1 = ball_position_temp;
        } else if ( *index == 'B' ) {
            ball_position_temp = ball_position_3;
            ball_position_3 = ball_position_2;
            ball_position_2 = ball_position_temp;
        } else if ( *index == 'C' ) {
            ball_position_temp = ball_position_3;
            ball_position_3 = ball_position_1;
            ball_position_1 = ball_position_temp;
        }
    }

    if ( ball_position_1 == 1 )
        return 1;
    else if ( ball_position_2 == 1 )
        return 2;
    else
        return 3;
    return 1;
}


TEST_CASE( "Input A should return 2", "[trik]" ) {
    REQUIRE( Trik((char*)"A") == 2);
}

TEST_CASE( "Input B should return 1", "[trik]" ) {
    REQUIRE( Trik((char*)'B') == 1);
}

TEST_CASE( "Input AB should return 3", "[trik]" ) {
    REQUIRE( Trik((char*)"AB") == 3 );
}

TEST_CASE( "Trik magic happened", "[trik]" ) {
    REQUIRE( Trik((char*)"CBABCACCC") == 1);
}
