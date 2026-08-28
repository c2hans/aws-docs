---
source_url: https://docs.aws.amazon.com/enclaves/latest/user/uninstall-acm.html
---

# Uninstall ACM for Nitro Enclaves
<a name="uninstall-acm"></a>

If you no longer want to use [AWS Certificate Manager for Nitro Enclaves](nitro-enclave-refapp.md), use the following procedure to uninstall it.

**To uninstall ACM for Nitro Enclaves**

1. Stop the web server.
   + **NGINX**

     ```
     $ sudo systemctl stop nginx
     ```
   + **Apache**

     ```
     $ sudo systemctl stop httpd
     ```

1. Stop the ACM for Nitro Enclaves service.

   ```
   $ sudo systemctl stop nitro-enclaves-acm.service
   ```

1. Uninstall ACM for Nitro Enclaves.

   ```
   $ sudo yum remove aws-nitro-enclaves-acm
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query enclaves` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
