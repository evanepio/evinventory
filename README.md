# evinventory

I'm using `pdm` to manage this project. Installing it using `brew`:

```
brew install pdm
```

You need to create an `.env` file:

```
DEBUG=True
SECRET_KEY=ThisShouldBeSuperSecretAndGeneratedFromScratch
```

And then run the server:

```
pdm run server
```