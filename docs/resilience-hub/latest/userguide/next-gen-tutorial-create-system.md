---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-tutorial-create-system.html
---

# Create a system
<a name="next-gen-tutorial-create-system"></a>

**Console:**

1. Open the the next generation of Resilience Hub console.

1. Choose **Systems** > **Create system**.

1. Enter a name (for example, `My Application`) and an optional description.

1. Choose **Create**.

**AWS CLI:**

```
aws resiliencehubv2 create-system \
  --name "my-application" \
  --description "My first application in Resilience Hub"
```
