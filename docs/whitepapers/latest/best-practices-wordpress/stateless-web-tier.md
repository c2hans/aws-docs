---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/stateless-web-tier.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Stateless web tier
<a name="stateless-web-tier"></a>

 To take advantage of multiple web servers in an automatic scaling configuration, your web tier must be stateless. A stateless application is one that needs no knowledge of previous interactions and stores no session information. In the case of WordPress, this means that all end users receive the same response, regardless of which web server processed their request. A stateless application can scale horizontally since any request can be serviced by any of the available compute resources (that is, web server instances). When that capacity is no longer required, any individual resource can be safely terminated (after running tasks have been drained). Those resources do not need to be aware of the presence of their peers – all that is required is a way to distribute the workload to them.

 When it comes to user session data storage, the WordPress core is completely stateless because it relies on cookies that are stored in the client’s web browser. Session storage isn’t a concern unless you have installed any custom code (for example, a WordPress plugin) that instead relies on native PHP sessions.

 However, WordPress was originally designed to run on a single server. As a result, it stores some data on the server’s local file system. When running WordPress in a multi-server configuration, this creates a problem because there is inconsistency across web servers. For example, if a user uploads a new image, it is only stored on one of the servers.

 This demonstrates why we need to improve the default WordPress running configuration to move important data to shared storage. The best practice architecture has a database as a separate layer outside the web server and makes use of shared storage to store user uploads, themes, and plugins.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
