import pytest
from parentheses_resolver.parentheses import parentheses_match, longest_parenthesis

class TestParenthesesMatch:
    def test_withEmptyString_shouldReturnTrue(self):
        # with
        empty = ""
        # when
        result = parentheses_match(empty)

        # then
        assert result

    def test_withOneParenthesesPair_shouldReturnTrue(self):
        # with
        one_pair = "()"
        # when
        result = parentheses_match(one_pair)

        # then
        assert result

    def test_withExclusivelyMatchingParentheses_shouldReturnTrue(self):
        # with
        multiple_pairs = "(((())(()())))()()"

        # when
        result = parentheses_match(multiple_pairs)

        # then
        assert result

    def test_withExpressionContainingMatchingParentheses_shouldReturnTrue(self):
        # with
        expression = "(((2+4) * 3) + ((3 - 6) * 4) ^ 2) / 7 + (5 - (6))*(4)"

        # when
        result = parentheses_match(expression)

        # then
        assert result

    def test_withOnlyOneOpenedParentheses_shouldReturnFalse(self):
        # with
        expression = "("

        # when
        result = parentheses_match(expression)

        # then
        assert result == False

    def test_withOnlyOneClosedParentheses_shouldReturnFalse(self):
        # with
        expression = ")"

        # when
        result = parentheses_match(expression)

        # then
        assert result == False

    def test_withMissingClosingParentheses_shouldReturnFalse(self):
        # with
        expression = "(())(()"

        # when
        result = parentheses_match(expression)

        # then
        assert result == False

    def test_withOneTooManyClosingParentheses_shouldReturnFalse(self):
        # with
        expression = "(()))"

        # when
        result = parentheses_match(expression)

        # then
        assert result == False

    def test_withUnmatchedParenthesesInExpression_shouldReturnFalse(self):
        # with
        expression = "(((2+4) * 3) + ((3 - 6) * 4) ^ 2) / 7 + (5 - )(6))*(4)"

        # when
        result = parentheses_match(expression)

        # then
        assert result == False

class TestLongestParentheses:
    def test_withEmptyString_shouldReturn0(self):
        # with
        expression = ""
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == 0

    def test_withSinglePair_shouldReturn2(self):
        # with
        expression = "()"
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == 2

    def test_withFilledSinglePair_shouldReturnlength(self):
        # with
        expression = "(1 + 3 + 4 * 7)"
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == len(expression)

    def test_withComplexExpression_shouldReturn4(self):
        # with
        expression = "() (()) ()"
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == 4


    def test_withUnMatchedParentheses_shouldReturn0(self):
        # with
        expression = "() (()) ("
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == 0
