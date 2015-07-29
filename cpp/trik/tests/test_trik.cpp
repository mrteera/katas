#include "trik.h"

#include "CppUTest/TestHarness.h"

TEST_GROUP(Trik)
{
    Trik* trik;

    void setup()
    {
        trik = new Trik();
    }

    void teardown()
    {
        delete trik;
    }
};

TEST(Trik, test_input_AB_should_return_3)
{
    int expected = 0;
    actual = trik.BallPosition("AAA");
    CHECK_EQUAL(expected, actual)
}
