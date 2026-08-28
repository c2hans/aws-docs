---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-react-example.html
---

# Example implementation of dynamic application management with React
<a name="integrate-aws-managed-apps-react-example"></a>

The following example demonstrates how to dynamically manage AWS-managed applications in a React application. This implementation uses `onAppHostAdded` and ` onAppHostRemoved` events to automatically update the user interface when applications are launched or destroyed. This example demonstrates how to position applications one after the other vertically on a web page.

## Iframe container component
<a name="integrate-aws-managed-apps-react-iframe-container"></a>

```
const IFrameAppContainer: React.FC<{ appHost: AppHost }> = ({ appHost }) => {
  const iframeRef = useRef<HTMLIFrameElement>(null);

  useEffect(() => {
    const iframe = iframeRef.current;
    if (iframe) {
      (appHost as IFrameAppHost).setIFrame(iframe);
    }
  }, [appHost]);

  const handleClose = (): void => {
    void appHost.destroy();
  };

  return (
    <div className="app-container">
      <div className="app-header">
        <h2>{appHost.config.name}</h2>
        <button onClick={handleClose}> Close </button>
      </div>
      <iframe ref={iframeRef} className="app-iframe" title={appHost.config.name} />
    </div>
  );
};
```

## Application container component
<a name="integrate-aws-managed-apps-react-app-container"></a>

```
const ApplicationContainer: React.FC<{provider: AmazonConnectProvider}>
  = ({provider}) => {

  const [activeApps, setActiveApps] = useState<Set<AppHost>>(new Set());

  useEffect(() => {
    const appManager = provider.appManager;

    // Handle new applications being added
    const handleAppHostAdded = ({appHost}: AppHostAdded): Promise<void> => {
      setActiveApps((prevApps) => new Set(prevApps).add(appHost));
      return Promise.resolve();
    };

    // Handle applications being removed
    const handleAppHostRemoved = ({appHost}: AppHostRemoved): Promise<void> => {
      setActiveApps((prevApps) => {
        const newApps = new Set(prevApps);
        newApps.delete(appHost);
        return newApps;
      });

      return Promise.resolve();
    };

    // Register event handlers
    appManager.onAppHostAdded(handleAppHostAdded);
    appManager.onAppHostRemoved(handleAppHostRemoved);

    return () => {
        // Un-register event handlers
        appManager.offAppHostAdded(handleAppHostAdded);
        appManager.offAppHostRemoved(handleAppHostRemoved);
    }

  }, [provider.appManager]);

  return (
    <div className="application-container">
      {Array.from(activeApps).map((appHost) => (
        <IFrameAppContainer key={appHost.instanceId} appHost={appHost} />
      ))}
    </div>
  );
};
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
