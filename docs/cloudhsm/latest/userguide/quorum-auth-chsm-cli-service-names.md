---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html
---

# Supported AWS CloudHSM service names and types for quorum authentication with CloudHSM CLI
<a name="quorum-auth-chsm-cli-service-names"></a>

**Admin Services**: Quorum authentication is used for admin privileged services like creating users, deleting users, changing user passwords, setting quorum values, and deactivating quorum and MFA capabilities.

**Crypto User Services**: Quorum authentication is used for crypto-user privileged services associated with a specific key like signing with a key, sharing/unsharing a key, wrapping/unwrapping a key, and setting a key's attribute. The quorum value of an associated key is configured when the key is generated, imported, or unwrapped. The quorum value must be equal to or less than the number of users that the key is associated with, which includes users that the key is shared with and the key owner.

Each service type is further broken down into a qualifying service name, which contains a specific set of quorum supported service operations that can be performed.

****

| Service name | Service type | Service operations |
| --- | --- | --- |
| user | Admin |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html)  |
| quorum | Admin |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html)  |
| cluster1 | Admin |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html)  |
| key-management | Crypto User |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html)  |
| key-usage | Crypto User |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-auth-chsm-cli-service-names.html)  |

[1] Cluster service is exclusively available on hsm2m.medium
