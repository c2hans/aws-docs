---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/download-function-package.html
---

# Download a function package from AWS TNB
<a name="download-function-package"></a>

Learn how to download a function package from the AWS TNB network functions catalog.

------
#### [ Console ]

**To download a function package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane on the left side of the console, choose **Function packages**.

1. Use search box to find the function package

1. Choose the function package

1. Choose **Actions**, **Download**.

------
#### [ AWS CLI ]

**To download a function package using the AWS CLI**
Use the [get-sol-function-package-content](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-function-package-content.html) command to download a function package.

```
aws tnb get-sol-function-package-content \
--vnf-pkg-id {{^fp-[a-f0-9]{17}$}} \
--accept "application/zip" \
--endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
--region {{us-west-2}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
