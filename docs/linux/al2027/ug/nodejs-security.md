---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/nodejs-security.html
---

# Security best practices
<a name="nodejs-security"></a>

 When using Node.js and *npm* on AL2027, follow the upstream [Node.js security best practices](https://nodejs.org/learn/getting-started/security-best-practices) guide on the Node.js website. It covers application-level threats, including supply chain attacks. It also covers mitigations, such as using lockfiles and disabling lifecycle scripts.

 Amazon Linux 2027 turns on npm's dependency cooldown by default. The *min-release-age* option (npm 11.10.0 and later) tells npm to resolve only package versions that have been publicly available for at least the given number of days, so a just-published — and possibly compromised — release cannot enter your dependency tree the moment it lands on the registry. Most malicious packages are detected and removed within hours, so even a short cooldown eliminates exposure to the majority of short-lived supply chain attacks. AL2027 sets a one-day cooldown in the system-wide npm configuration file, */etc/npmrc*:

```
min-release-age=1
```

 The value is expressed in days, so by default every npm install and npm update on the instance ignores versions published in the last 24 hours. You do not need to edit */etc/npmrc* to change this: it is npm's lowest-precedence configuration source, and any higher-precedence source overrides it — the command line, npm\_config\_\* environment variables, a project-level *.npmrc*, or a user-level *\~/.npmrc*. Raise the value for a stricter policy, or set it to 0 to disable the cooldown for a single command:

```
npm install --min-release-age=0 package-name
```

 Use that per-command override when you need a security fix that was published inside the cooldown window. Run

```
npm audit
```

 to identify which dependencies have known vulnerabilities and require immediate updating. Note that if the cooldown leaves no eligible version for a dependency, npm fails the command rather than silently selecting a different release — override the cooldown for that install or pin the dependency explicitly.
