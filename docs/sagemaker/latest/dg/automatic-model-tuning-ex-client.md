---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-client.html
---

# Get the Amazon SageMaker AI Boto 3 Client
<a name="automatic-model-tuning-ex-client"></a>

Import Amazon SageMaker Python SDK, AWS SDK for Python (Boto3), and other Python libraries. In a new Jupyter notebook, paste the following code to the first cell:

```
import sagemaker
import boto3

import numpy as np                                # For performing matrix operations and numerical processing
import pandas as pd                               # For manipulating tabular data
from time import gmtime, strftime
import os

region = boto3.Session().region_name
smclient = boto3.Session().client('sagemaker')
```

The preceding code cell defines `region` and `smclient` objects that you will use to call the built-in XGBoost algorithm and set the SageMaker AI hyperparameter tuning job.

## Next Step
<a name="automatic-model-tuning-ex-next-role"></a>

[Get the SageMaker AI Execution Role](automatic-model-tuning-ex-role.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
