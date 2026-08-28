---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/nodejs-library-reference.html
---

# NodeJS library reference
<a name="nodejs-library-reference"></a>

 The key step in the process of integrating the solution with your architecture involves incorporating token management methods with the services that you expose to the client’s application directly. When you launch the API module an example API endpoint that acts as such service is created but in your actual implementation you may be tasked with adding token management operations into your workflow comprised of preexisting services. This solution comes with a NodeJS library, which facilitates this procedure by abstracting the token management operations that need to take place with code constructs that you can import in your own code. This section defines how the solution’s NodeJS library has been structured, what classes and methods are made available for use and provide detailed reference of usage specific constructs included in the library.

## On a high level
<a name="on-a-high-level"></a>

 The library is provided as a single module that you can import with a single import command. From the module we expose all functionalities you interact with through classes. These classes are:
+  Secret - to manage the keys used for signing and validating the tokens
+  Token - to manage the token generation process
+  Session - to manage viewer sessions when generating token and revoking the session

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
