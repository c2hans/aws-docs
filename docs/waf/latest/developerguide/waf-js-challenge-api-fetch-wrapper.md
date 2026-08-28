---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-fetch-wrapper.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# How to use the integration `fetch` wrapper
<a name="waf-js-challenge-api-fetch-wrapper"></a>

This section provides instructions for using the integration `fetch` wrapper.

You can use the AWS WAF `fetch` wrapper by changing your normal `fetch` calls to the `fetch` API under the `AwsWafIntegration` namespace. The AWS WAF wrapper supports all of the same options as the standard JavaScript `fetch` API call and adds the token handling for the integration. This approach is generally the simplest way to integrate your application.

**Before the wrapper implementation**
The following example listing shows standard code before implementing the `AwsWafIntegration` `fetch` wrapper.

```
const login_response = await fetch(login_url, {
	    method: 'POST',
	    headers: {
	      'Content-Type': 'application/json'
	    },
	    body: login_body
	  });
```

**After the wrapper implementation**
The following listing shows the same code with the `AwsWafIntegration` `fetch` wrapper implementation.

```
const login_response = await AwsWafIntegration.fetch(login_url, {
	    method: 'POST',
	    headers: {
	      'Content-Type': 'application/json'
	    },
	    body: login_body
	  });
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
