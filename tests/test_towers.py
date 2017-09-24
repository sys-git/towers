#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# @module tests.test_towers
# @version 0.1
# @copyright (c) 2017-present Francis Horsman.

from __future__ import print_function

import json
import unittest

from towers import Towers


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_run(self, height=3, verbose=True):
        assert height >= 1, height

        tower = Towers(height, verbose=verbose)

        print(tower)
        print('moves required: {moves}'.format(moves=tower.moves_for_height(height)))

        with tower:
            for i in tower:
                print(i)

        print(tower)
        print('moves taken: {moves}'.format(moves=tower.moves))

        x = json.dumps(tower, cls=Towers.JsonEncoder)
        y = Towers.from_json(x)
        print(y)

        self.assertEqual(tower, y)

    def test_context(self, height=3, verbose=True):
        tower = Towers(height, verbose=verbose)
        tower_old = Towers.from_json(tower.to_json())
        print(tower)

        with tower.context():
            for _ in tower:
                pass

            tower_new = tower.to_json()
            self.assertNotEqual(tower_new, tower_old)

        print(tower)
        self.assertEqual(tower_old, tower)
        self.assertNotEqual(tower_new, tower)


if __name__ == '__main__':
    unittest.main()
