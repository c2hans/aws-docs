---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/python-driver-install.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Installing the Amazon Redshift Python connector
<a name="python-driver-install"></a>

You can use any of the following methods to install the Amazon Redshift Python connector:
+ Python Package Index (PyPI)
+ Conda
+ Cloning the GitHub repository

## Installing the Python connector from PyPI
<a name="python-pip-install-pypi"></a>

To install the Python connector from the Python Package Index (PyPI), you can use pip. To do this, run the following command.

```
>>> pip install redshift_connector
```

You can install the connector within a virtual environment. To do this, run the following command.

```
>>> pip install redshift_connector
```

Optionally, you can install pandas and NumPy with the connector.

```
>>> pip install 'redshift_connector[full]'
```

For more information on pip, see the [pip site](https://pip.pypa.io/en/stable/).

## Installing the Python connector from Conda
<a name="python-pip-install-from-conda"></a>

You can install the Python connector from Anaconda.org.

```
>>>conda install -c conda-forge redshift_connector
```

## Installing the Python connector by cloning the GitHub repository from AWS
<a name="python-pip-install-from-source"></a>

To install the Python connector from source, clone the GitHub repository from AWS. After you install Python and virtualenv, set up your environment and install the required dependencies by running the following commands.

```
$ git clone https://github.com/aws/amazon-redshift-python-driver.git
$ cd amazon-redshift-python-driver
$ virtualenv venv
$ . venv/bin/activate
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
$ python -m pip install redshift_connector
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
