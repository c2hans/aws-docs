---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-rules.html
---

# Rules and limits
<a name="config-conductor-live-rules"></a>

The following table provides a summary of the configuration rules and constraints that apply to an AWS Elemental Conductor Live cluster.

- ** Hardware in a cluster **
  - A Conductor Live cluster can include a maximum of 50 worker nodes.

- ** Physical location of nodes in a cluster **
  - Within a cluster, the Conductor Live and encoder nodes must be located in the same physical location.
  - Within a cluster, the communications among cluster members shouldn't traverse the public internet.
