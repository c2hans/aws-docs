---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrio/deploy-docker.html
---

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Step 3: Deploy and configure the Docker container
<a name="deploy-docker"></a>

Complete the following procedure to deploy and configure the Docker container.

1. Start the Docker image on your host:

   ```
   docker run -v ~/WickrIO:/opt/WickrIO -ti public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest
   ```

1. Select your preference for the welcome message.
![The Wickr IO welcome message prompt.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickrio-welcome-message-prompt.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
