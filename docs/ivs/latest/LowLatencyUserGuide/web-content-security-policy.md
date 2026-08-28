---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/web-content-security-policy.html
---

# Working With Content Security Policy
<a name="web-content-security-policy"></a>

The Amazon IVS Web player SDK is configured to work on pages that use Content Security Policy (CSP). A few key CSP directives must be in place. Here, we describe a minimal set of directives that are necessary. Additional directives and sources are likely necessary, depending on your specific setup.

The following directives are the minimum required for CSP:

```
worker-src blob:;
media-src blob:;
connect-src *.live-video.net;
script-src 'wasm-unsafe-eval';
```

**Note:** Older versions of browsers may not recognize one or more of those above CSP rules (such as `wasm-unsafe-eval`) and instead could require a very lenient CSP policy (`unsafe-eval`). However, that works against the whole point of CSP to limit dangerous JavaScript from running on a page. Instead, as a workaround, we recommend that you host the library assets on the same origin as your page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
