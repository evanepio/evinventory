# evinventory

I'm using `pdm` to manage this project. Installing it using `brew`:

```
brew install pdm
```

You need to create an `.env` file:

```
DJANGO_SETTINGS_MODULE=evinventory.django.local
EVAN_DEBUG=True
EVAN_SECRET_KEY=ThisShouldBeSuperSecretAndGeneratedFromScratch
```

If you want to generate a secret key for the `.env` file, just run the following:

```
pdm generate-key
```

You'll need to do the migrations:

```
pdm manage migrate
```

> The `pdm migrate` will run the `manage.py` script with the `.env` file.

And then run the server:

```
pdm server
```