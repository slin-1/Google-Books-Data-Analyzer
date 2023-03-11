# check_equal
# Version 1.0 11/04/22
# Developed by: Steven Lin, Brady Thompson, Nolan Wrigley, and Fisher Walsh

# Testing Function
def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    Returns 1 if "passed"
    Returns 0 if "failed"
    """
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:    
        print("{0} FAILED: \nExpected: \n({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        print("------")
        return 0
    
    elif outcome != expected:
        print("{0} FAILED: \nExpected: \n{1}, \nGot: \n{2}".
              format(description, expected, outcome))
        print("------")
        return 0
    
    else:
        print("{0} PASSED".format(description))
        print("------")
        return 1