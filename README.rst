|version| |ci| |coverage| |license|

things-cli
======
Command-line interface for `Things 3 <https://culturedcode.com/things/>`_.

Due to limited integration functionality (no public API), the only interesting feature for now is to create TODOs from emails.
Sadly, no projects, tags or contexts are supported yet.

Getting Started
---------------

Install

.. code:: shell

    pip install things-cli

Run

.. code:: shell

    things add "Buy milk" "Low-fat, please"

.. |version| image:: https://img.shields.io/pypi/v/things-cli.svg
   :target: https://pypi.python.org/pypi/things-cli/
.. |ci| image:: https://api.travis-ci.org/amureki/things-cli.svg?branch=master
   :target: https://travis-ci.org/amureki/things-cli
.. |coverage| image:: https://codecov.io/gh/amureki/things-cli/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/amureki/things-cli
.. |license| image:: https://img.shields.io/badge/license-Apache_2-blue.svg
   :target: LICENSE