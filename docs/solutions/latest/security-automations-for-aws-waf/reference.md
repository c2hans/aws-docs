---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution, pointers to [related resources](#related-resources), and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When turned on, the solution collects the following information is collected and sends it to AWS during initial deployment of the CloudFormation template:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each deployment of this solution
+  **Timestamp** - Data-collection timestamp
+  **Solution configuration** - Features turned on and parameters set during initial launch
+  **Lifecycle** - How long the customer used this solution (based on stack delete)
+  **Log parser data**:
  + The number of IP addresses in the **Scanner & Probe** IP set, **Bad Bot** IP set and the **HTTP Flood** IP set to block
  + The number of requests processed and blocked
+  **IP lists parser data**:
  + The number of IP addresses in the **Reputation Lists** IP set
  + The number of requests processed and blocked
+  **IP retention data** - The number of expired IP addresses being removed from the **Allowed** or **Denied** IP set

AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the `aws-waf-security-automations.template` [AWS CloudFormation](aws-cloudformation-templates.md) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Modify the CloudFormation template mapping section from:

   ```
   Solution:
     Data:
      SendAnonymizedUsageData: "Yes"
   ```

   to:

   ```
   Solution:
     Data:
      SendAnonymizedUsageData: "No"
   ```

1. Sign in the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Step 1. Launch the stack](step-1.-launch-the-stack.md).

## Related resources
<a name="related-resources"></a>

### Associated AWS whitepapers
<a name="associated-aws-whitepapers"></a>
+  [AWS Best Practices for DDoS Resiliency](https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)

### Associated AWS Security Blog posts
<a name="associated-aws-security-blog-posts"></a>
+  [How to Prevent Hotlinking by Using AWS WAF, Amazon CloudFront, and Referer Checking](https://aws.amazon.com/blogs/security/how-to-prevent-hotlinking-by-using-aws-waf-amazon-cloudfront-and-referer-checking/)

### Third-Party IP Reputation Lists
<a name="third-party-ip-reputation-lists"></a>
+  [Spamhaus DROP List website](https://www.spamhaus.org/drop/)
+  [Proofpoint Emerging Threats IP list](https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt)
+  [Tor exit node list](https://check.torproject.org/exit-addresses)

## Contributors
<a name="contributors"></a>
+ Heitor Vital
+ Lee Atkinson
+ Ben Potter
+ Vlad Vlasceanu
+ Aijun Peng
+ Chaitanya Deolankar
+ Shu Jackson
+ William Quan
+ Mykhailo Markhain
