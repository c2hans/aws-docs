---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/conditional-transformation-issues.html
---

# Conditional transformation issues
<a name="conditional-transformation-issues"></a>

 **Symptoms:** - Conditional transformations not triggering - Wrong transformation applied based on conditions - Client hints not being evaluated correctly

 **Solutions:**

 **Review condition syntax:**
+ Verify field names match available headers
+ Check condition values and operators
+ Ensure client is sending required headers

 **Test condition logic:**
+ Use Admin UI testing tools to validate conditions
+ Check request headers in browser developer tools
+ Verify condition evaluation in ECS task logs
