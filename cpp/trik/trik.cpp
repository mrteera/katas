/* http://programming.in.th/task/rev2_problem.php?pid=0010 */
#define CATCH_CONFIG_MAIN
#include "../catch.hpp"
using namespace std;


int Trik( string cipher ) {
    int ball_position = 1;
    int index;
    
    for ( index = 0; index < cipher.length(); index++ ) {
        ball_position++;
    }

    return ball_position;
}


TEST_CASE( "Trik magic happened", "[trik]" ) {
    REQUIRE( Trik("AB") == 3 );
    REQUIRE( Trik("A") == 2);
    //REQUIRE( Trik("CBABCACCC") == 1);
}
