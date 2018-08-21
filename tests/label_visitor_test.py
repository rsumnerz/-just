import unittest
from label_visitor import LabelVisitor
from ast import parse

class LabelVisitorTestCase(unittest.TestCase):
    '''Baseclass for LabelVisitor tests'''

    def perform_labeling_on_expression(self, expr):
        obj = parse(expr)
        label = LabelVisitor()
        label.visit(obj)

        return label

class LabelVisitorTest(LabelVisitorTestCase):
    def test_assign(self):
        label = self.perform_labeling_on_expression('a = 1')
        self.assertEqual(label.result,'a = 1')

    def test_compare(self):
        label = self.perform_labeling_on_expression('a > b')
        self.assertEqual(label.result,'a > b')

    def test_binop(self):
        label = self.perform_labeling_on_expression('a / b')
        self.assertEqual(label.result,'a / b')
