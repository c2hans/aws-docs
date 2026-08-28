---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_env.html
---

# Example: Set global environment variables for AWS PCS
<a name="working-with_ec2-user-data_env"></a>

 Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md).

The following example uses `/etc/profile.d` to set global variables on node group instances.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
touch /etc/profile.d/awspcs-userdata-vars.sh
echo MY_GLOBAL_VAR1=100 >> /etc/profile.d/awspcs-userdata-vars.sh
echo MY_GLOBAL_VAR2=abc >> /etc/profile.d/awspcs-userdata-vars.sh

--==MYBOUNDARY==--
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
