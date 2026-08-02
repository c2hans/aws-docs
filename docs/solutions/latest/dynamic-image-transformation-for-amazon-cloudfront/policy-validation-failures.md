---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/policy-validation-failures.html
---

# Policy validation failures
<a name="policy-validation-failures"></a>

 **Symptoms:** - 400 Bad Request errors when creating policies - Policy creation fails in Admin UI - "Invalid policy JSON" error messages

 **Solutions:**

 **Check JSON syntax:**
+ Validate JSON structure using online JSON validators
+ Ensure all required fields are present
+ Verify transformation parameter types match schema requirements

 **Review transformation limits:** - Policy size limit: 400KB - Ensure transformation values are within valid ranges
