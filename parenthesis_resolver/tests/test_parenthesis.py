import pytest
from parenthesis import parenthesis_match, longest_parenthesis

class TestParenthesisMatch:
    def test_withEmptyString_shouldReturnTrue(self):
        # with
        empty = ""
        # when
        result = parenthesis_match(empty)

        # then
        assert result

    def test_withOneParenthesisPair_shouldReturnTrue(self):
        # with
        one_pair = "()"
        # when
        result = parenthesis_match(one_pair)

        # then
        assert result

    def test_withExclusivelyMatchingParenthesis_shouldReturnTrue(self):
        # with
        multiple_pairs = "(((())(()())))()()"

        # when
        result = parenthesis_match(multiple_pairs)

        # then
        assert result

    def test_withExpressionContainingMatchingParenthesis_shouldReturnTrue(self):
        # with
        expression = "(((2+4) * 3) + ((3 - 6) * 4) ^ 2) / 7 + (5 - (6))*(4)"

        # when
        result = parenthesis_match(expression)

        # then
        assert result

    def test_withOnlyOneOpenedParenthesis_shouldReturnFalse(self):
        # with
        expression = "("

        # when
        result = parenthesis_match(expression)

        # then
        assert result == False

    def test_withOnlyOneClosedParenthesis_shouldReturnFalse(self):
        # with
        expression = ")"

        # when
        result = parenthesis_match(expression)

        # then
        assert result == False

    def test_withMissingClosingParenthesis_shouldReturnFalse(self):
        # with
        expression = "(())(()"

        # when
        result = parenthesis_match(expression)

        # then
        assert result == False

    def test_withOneTooManyClosingParenthesis_shouldReturnFalse(self):
        # with
        expression = "(()))"

        # when
        result = parenthesis_match(expression)

        # then
        assert result == False

    def test_withUnmatchedParenthesisInExpression_shouldReturnFalse(self):
        # with
        expression = "(((2+4) * 3) + ((3 - 6) * 4) ^ 2) / 7 + (5 - )(6))*(4)"

        # when
        result = parenthesis_match(expression)

        # then
        assert result == False

class TestLongestParenthesis:
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


    def test_withUnMatchedParenthesis_shouldReturn0(self):
        # with
        expression = "() (()) ("
        # when
        result = longest_parenthesis(expression)

        # then
        assert result == 0
