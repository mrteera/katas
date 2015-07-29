/* http://programming.in.th/task/rev2_problem.php?pid=0010 */
#define CATCH_CONFIG_MAIN
#include "../catch.hpp"
using namespace std;


int Trik( string cipher ) {
    if ( cipher == "A" )
        return 2;
    else
        return 3;
}


TEST_CASE( "Trik magic happened", "[trik]" ) {
    REQUIRE( Trik("AB") == 3 );
    REQUIRE( Trik("A") == 2);
    //REQUIRE( Trik("CBABCACCC") == 1);
}
