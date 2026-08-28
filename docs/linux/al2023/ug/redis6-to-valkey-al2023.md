---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/redis6-to-valkey-al2023.html
---

# Tutorial: Redis 6 to Valkey Transition on AL2023
<a name="redis6-to-valkey-al2023"></a>

The following documentation describes key aspects of the transition from Redis 6 to Valkey on AL2023.

## Support timeline for Redis 6
<a name="redis6-support-al2023"></a>

 Redis 6 reaches its End of Life (EOL) on January 31, 2027. After this date, Redis 6 will no longer receive updates or security patches from the Redis project. We strongly recommend users migrate to Valkey before January 2027 to ensure continued support and security updates.

 For more information on Redis version support timelines, see [Redis End-Of-Life Schedule](https://github.com/redis/redis?tab=security-ov-file#security-policy) documentation.

## Introduction to Valkey
<a name="valkey-introduction-al2023"></a>

 Valkey is an open-source fork of Redis 7, maintained by The Linux Foundation. It's fully compatible with Redis Open Source Software (OSS) versions 2.x through 7.2.x. Valkey maintains the familiar Redis API and functionality while offering several enhancements:
+ Enhanced performance through multi-threading.
+ Improved memory efficiency, especially in cluster mode.
+ Dual-channel replication for better data consistency.

## Migration plan and timeline
<a name="valkey-migration-plan-timeline-al2023"></a>

 Users are strongly encouraged to migrate from Redis 6 to Valkey before January 31, 2027, when Redis 6 reaches its End of Life (EOL). This migration requires manual intervention and is not automatic.

 Amazon Linux recommends this migration to ensure continued functionality, support, and security updates for your Redis-dependent applications.

## Migration options and steps
<a name="valkey-migration-option-steps-al2023"></a>

 We propose three migration paths to Valkey based on your deployment requirements and operational needs.

### Option 1: New Instance Installation
<a name="new-instance-installation"></a>

For new deployments or when data migration is not needed:

1. Install Valkey:

   ```
   [ec2-user ~]$ sudo dnf install valkey
   ```

1. Start Valkey:

   ```
   [ec2-user ~]$ sudo systemctl start valkey
   ```

1. (Optional) Enable Valkey on boot:

   ```
   [ec2-user ~]$ sudo systemctl enable valkey
   ```

1. Verify the installation:

   ```
   [ec2-user ~]$ valkey-cli info server
   [ec2-user ~]$ valkey-cli ping
   ```

### Option 2: In-Place Replacement
<a name="in-place-replacement"></a>

For existing instances where data persistence is not required:

1. Stop Redis 6:

   ```
   [ec2-user ~]$ sudo systemctl stop redis6
   ```

1. Install Valkey:

   ```
   [ec2-user ~]$ sudo dnf install valkey
   ```

1. (Optional) Use Redis 6 configuration in Valkey:

   ```
   [ec2-user ~]$ sudo cp /etc/redis6/redis6.conf /etc/valkey/valkey.conf
   [ec2-user ~]$ sudo cp /etc/valkey/valkey.conf /etc/valkey/valkey.conf.backup
   [ec2-user ~]$ sudo chown valkey:root /etc/valkey/valkey.conf
   [ec2-user ~]$ sudo sed -i 's|^dir\s.*|dir /var/lib/valkey|g' /etc/valkey/valkey.conf
   ```

1. (Optional) Use Redis 6 sentinel configuration file in Valkey:

   ```
   [ec2-user ~]$ sudo cp /etc/redis6/sentinel.conf /etc/valkey/sentinel.conf
   [ec2-user ~]$ sudo chown valkey:root /etc/valkey/sentinel.conf
   ```

1. Start Valkey:

   ```
   [ec2-user ~]$ sudo systemctl start valkey
   ```

1. (Optional) Enable Valkey on boot:

   ```
   [ec2-user ~]$ sudo systemctl enable valkey
   ```

1. Verify Valkey installation:

   ```
   [ec2-user ~]$ valkey-cli info server
   [ec2-user ~]$ valkey-cli ping
   ```

1. Remove Redis 6:

   ```
   [ec2-user ~]$ sudo dnf remove redis6
   ```

### Option 3: Data Migration
<a name="data-migration"></a>

This option allows you to run both Redis 6 and Valkey concurrently.

1. Install Valkey without removing Redis 6:

   ```
   [ec2-user ~]$ sudo dnf install valkey
   ```

1. (Optional) Use Redis 6 configuration in Valkey:

   ```
   [ec2-user ~]$ sudo cp /etc/redis6/redis6.conf /etc/valkey/valkey.conf
   [ec2-user ~]$ sudo cp /etc/valkey/valkey.conf /etc/valkey/valkey.conf.backup
   [ec2-user ~]$ sudo chown valkey:root /etc/valkey/valkey.conf
   [ec2-user ~]$ sudo sed -i 's|^dir\s.*|dir /var/lib/valkey|g' /etc/valkey/valkey.conf
   ```

1. (Optional) Use Redis 6 sentinel configuration file in Valkey:

   ```
   [ec2-user ~]$ sudo cp /etc/redis6/sentinel.conf /etc/valkey/sentinel.conf
   [ec2-user ~]$ sudo chown valkey:root /etc/valkey/sentinel.conf
   ```

1. Modify Valkey configuration:

   Edit `/etc/valkey/valkey.conf` and set the 'port' directive to a different value (for example, 6380) to avoid conflicts with Redis 6.

1. Start Valkey:

   ```
   [ec2-user ~]$ sudo systemctl start valkey
   ```

1. (Optional) Enable Valkey on boot:

   ```
   [ec2-user ~]$ sudo systemctl enable valkey
   ```

1. Verify Valkey installation:

   ```
   [ec2-user ~]$ valkey-cli -p {{port}} info server
   [ec2-user ~]$ valkey-cli -p {{port}} ping
   ```
**Note**
Replace {{port}} with the configured port number.

1. Migrate data:

   You can now migrate data from Redis 6 to Valkey using replication or manual data transfer methods.

1. Update application configurations:

   Gradually update your applications to use the Valkey port.

1. Remove Redis 6:

   Once all data and applications have been migrated, you can stop and remove Redis 6.

   ```
   [ec2-user ~]$ sudo systemctl stop redis6
   [ec2-user ~]$ sudo dnf remove redis6
   ```

**Note**
 It is strongly recommended to validate the migration process in a test environment before implementing changes in production systems.

## Related topics
<a name="valkey-migration-related-topics-al2023"></a>

 For more information about Valkey:
+ Valkey: [https://valkey.io/](https://valkey.io)
+ Valkey migration: [https://valkey.io/topics/migration/](https://valkey.io/topics/migration/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
