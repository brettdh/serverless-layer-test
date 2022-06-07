# Serverless + layers behavior test / bug repro

This repo contains a couple serverless apps and scripts to test/repro some odd behaviors.

## Plain

The `plain-layer-test` app is a very simple setup:

- `handler.py`: stock hello-world lambda, calling functions defined in a layer
- `layer/hello_layer.py`: defines functions; gets packaged into a layer

The test script:
1. deploys the lambda + layer with a single layer function
2. calls the lambda
3. deploys the lambda + layer again, with an additional function defined in the layer
   - Optionally, if the first positional argument to the script is `function`,
     this second deploy will deploy _only_ the `hello` function, not the whole app
4. calls the lambda again, checking whether the layer was updated


### Notes
- This test succeeds when the whole app is deployed.
- It fails when just the function is deployed (after changing the layer).


## Reqs

The `reqs-layer-test` app adds [serverless-python-requirements] to the mix,
building a lambda layer from a `requirements.txt` file.

- `handler.py`: stock hello-world lambda, importing packages installed in `/opt`
- `requirements.txt`: defines packages to be made available in `/opt`

The test script:
1. deploys the lambda + layer with a single package, `arrow`
2. calls the lambda
3. deploys the lambda + layer again, with an additional package, `pendulum`
   - Optionally, if the first positional argument to the script is `function`,
     this second deploy will deploy _only_ the `hello` function, not the whole app
   - Before doing this, we delete a file to work around [upstream issue 278].
4. calls the lambda again, checking whether the layer was updated

### Notes
- This test fails regardless of whether the second deploy is the whole app or just the function.


## Detailed results
The `logs/` folder in each app folder contains verbose logs from these test runs:

- `plain-layer-test/`
  - :white_check_mark: `./run_test -v`
  - :x: `./run_test -v function`
- `reqs-layer-test/`
  - :x: `./run_test -v`
  - :x: `./run_test -v function`

[serverless-python-requirements]: https://github.com/serverless/serverless-python-requirements/
[upstream issue 278]: https://github.com/serverless/serverless-python-requirements/issues/278
