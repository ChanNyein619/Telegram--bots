"""
Tests for the chatterbot corpus package.
"""
import os
import io
from unittest import TestCase
from chatterbot import corpus


class CorpusUtilsTestCase(TestCase):

    def test_get_file_path(self):
        """
        Test that a dotted path is properly converted to a file address.
        """
        path = corpus.get_file_path('chatterbot.corpus.english')
        self.assertIn(
            os.path.join('chatterbot_corpus', 'data', 'english'),
            path
        )

    def test_read_english_corpus(self):
        corpus_path = os.path.join(
            corpus.DATA_DIRECTORY,
            'english', 'conversations.yml'
        )
        data = corpus.read_corpus(corpus_path)
        self.assertIn('conversations', data)

    def test_list_english_corpus_files(self):
        data_files = corpus.list_corpus_files('chatterbot.corpus.english')

        self.assertIn('.yml', data_files[0])

    def test_load_english_corpus(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/english/greetings.yml')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertEqual(len(corpus_data), 1)
        self.assertIn(['Hi', 'Hello'], corpus_data[0][0])

    def test_load_english_corpus_categories(self):
        files = corpus.list_corpus_files('chatterbot_corpus/data/english/greetings.yml')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertEqual(len(corpus_data), 1)

        # Test that each conversation gets labeled with the correct category
        for conversation in corpus_data:
            self.assertIn('greetings', conversation[1])
