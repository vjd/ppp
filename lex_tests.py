import unittest

class ExecuteTest(unittest.TestCase):

  def setUp(self):
    self.input = (
        "efg\n",
        "A\n",
        "Bcd\n",
        "aa\n",
        "abc\n"
        )

  def test_lex_logic_insensitive(self):
      """
        test whether the insensitive flag works for lex_sort.py
        do this by checking if the output lists with and without the
        the insensitive flag are similar
      """
      lines = sorted(self.input)
      lines_insensitive = sorted(self.input, key=lambda y: y.lower())
      self.assertNotEqual(lines,lines_insensitive)

  def test_lex_logic_nline(self):
      """
      test whether the nline option returns requested number of lines
      :return:
      """
      nline=3
      lines = sorted(self.input)
      lines_insensitive = sorted(self.input, key=lambda y: y.lower())
      out_line = []
      for i in range(nline):
        out_line.append(lines[i])

      self.assertEqual(nline,len(out_line))

if __name__ == '__main__':
  unittest.main()
