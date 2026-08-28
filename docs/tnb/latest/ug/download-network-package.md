---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/download-network-package.html
---

# Download a network package from AWS TNB
<a name="download-network-package"></a>

Learn how to download a network package from the AWS TNB network service catalog.

------
#### [ Console ]

**To download a network package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network packages**.

1. Use the search box to find the network package

1. Choose the network package.

1. Choose **Actions**, **Download**.

------
#### [ AWS CLI ]

**To download a network package using the AWS CLI**
+ Use the [get-sol-network-package-content](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-network-package-content.html) command to download a network package.

  ```
  aws tnb get-sol-network-package-content \
  --nsd-info-id {{^np-[a-f0-9]{17}$}} \
  --accept "application/zip" \
  --endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
  --region {{us-west-2}}
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
