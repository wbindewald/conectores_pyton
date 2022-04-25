# Eleflow Spark Connector
Multiple app connector for use with spark
---

## Software architecture

All connectors need follow some rules, that way is guaranteed the same skeleton and first steps definitions for whole sub-modules.

When the sub-module is an API abstraction, follow these patterns:

### The ConnectionClass must will be exported in ```__init__.py``` and provide the only front door for the use and them must be required the credentials for the connection.
```
    class SubModuleConnection:

        def __init__(self, args):
            ...

        @classmethod
        def build_from_credentials(cls, credentials):
            return cls(...)

        def get_service_client(self):
            return SubModuleServiceClient(...)

```

### The ServiceClient must provide all services that the users can call
```
    class SubModuleServiceClient():

        def __init__(self, args):
            ...

        def get_something_caller(self, args):
            return GetSomethingCaller(args)

```

### The caller class must be a subclaas from RestBase that provide all http methods already implemented and ready to be used
```
    class SubModuleCaller(Restbase):

        def __init__(self, args):
            ...

        def get_something(self, *args, **kwargs):
            return self.get(args, kwargs)

        def post_something(self, data):
            return self.post(data, *())
        
```