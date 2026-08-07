# Changelog

All notable changes to this project are documented in this file.

## [0.2.0](https://github.com/lexmiin/evocomp/compare/v0.1.0..v0.2.0) - 2026-08-07

### Changes

- algorithms: add functional facades for min/max optimizers by [@lexmiin](https://github.com/lexmiin) ([a5dfd73](https://github.com/lexmiin/evocomp/commit/a5dfd7366093d0c98f1dc1b129c3b75e216d6afb))


### Documentation

- docs: move development section to the bottom of readme by [@lexmiin](https://github.com/lexmiin) ([f062897](https://github.com/lexmiin/evocomp/commit/f062897574a58ccc280e97b2a53d81d51e15b61f))


### Internal

- chore: prefix private methods with single underscore by [@lexmiin](https://github.com/lexmiin) ([91bc948](https://github.com/lexmiin/evocomp/commit/91bc94849cd9a25e2c5397f7b44b26bac569c83f))

## [0.1.0] - 2026-08-07

### Changes

- feat: initial commit by [@lexmiin](https://github.com/lexmiin) ([4a43add](https://github.com/lexmiin/evocomp/commit/4a43add519b64d13323367199fee181d9cf52215))
- feat: algo and lib packages by [@lexmiin](https://github.com/lexmiin) ([dd52bb3](https://github.com/lexmiin/evocomp/commit/dd52bb30ecbc97393bb0141dfc6bc1181d944bdd))
- feat: export data into csv or excel by [@lexmiin](https://github.com/lexmiin) ([b1ffacf](https://github.com/lexmiin/evocomp/commit/b1ffacf454b2b5daaac9058bd5706b7c75477796))
- feat: create config parsed from cli arguments by [@lexmiin](https://github.com/lexmiin) ([21d185d](https://github.com/lexmiin/evocomp/commit/21d185dcd992d7e6e1b2414fea129afd44ba19b1))
- feat(config): add dimension option, use plot with default value false by [@lexmiin](https://github.com/lexmiin) ([86db615](https://github.com/lexmiin/evocomp/commit/86db61586c49fceaf5fcdde91862996cb3f703a2))
- feat(constants): add list of 1D and ND test functions by [@lexmiin](https://github.com/lexmiin) ([ed2fb0d](https://github.com/lexmiin/evocomp/commit/ed2fb0d6379efff8f4376a15027429f825931f15))
- feat(common): add `get_random_indexes` function by [@lexmiin](https://github.com/lexmiin) ([eb298a7](https://github.com/lexmiin/evocomp/commit/eb298a79735b37305fb26a88a3c14b041cca9576))
- feat(algo): implement fractal structurization algorithm by [@lexmiin](https://github.com/lexmiin) ([90d2ab4](https://github.com/lexmiin/evocomp/commit/90d2ab45577e1ab91e9192139b0a1d01d7d20684))
- feat(algo): implement aco algorithm by [@lexmiin](https://github.com/lexmiin) ([2892542](https://github.com/lexmiin/evocomp/commit/2892542373d61743479f9ff0a5c5143eb16dc263))
- feat: add genetic programming algo by [@lexmiin](https://github.com/lexmiin) ([7dfb8a8](https://github.com/lexmiin/evocomp/commit/7dfb8a8029e549b25da64a47dd72ed322e29354c))
- feat: add script to generate delivery data by [@lexmiin](https://github.com/lexmiin) ([590bd5e](https://github.com/lexmiin/evocomp/commit/590bd5e7f6f50c592eece4669975e385636a6494))
- feat: add parcel delivery solver by [@lexmiin](https://github.com/lexmiin) ([cf0d899](https://github.com/lexmiin/evocomp/commit/cf0d899b760977de564427bc8844ddc87fbb90c4))
- refactor: update `Stats` `record_solution` method, access `param_value` by [@lexmiin](https://github.com/lexmiin) ([bd6bf28](https://github.com/lexmiin/evocomp/commit/bd6bf289b3e91256266c60776ccbbd7f0bda8e20))
- feat: inject `Stats` object into algorithms by [@lexmiin](https://github.com/lexmiin) ([7c73be7](https://github.com/lexmiin/evocomp/commit/7c73be7f7db270ca1685113230655d3034d229c0))
- feat: add default config for algorithms using yaml by [@lexmiin](https://github.com/lexmiin) ([3348fbd](https://github.com/lexmiin/evocomp/commit/3348fbd5130a4a55f32d89fd249695677196270d))
- refactor: rename `get_config` to `read_cli` by [@lexmiin](https://github.com/lexmiin) ([78ce603](https://github.com/lexmiin/evocomp/commit/78ce603cf04328695d3e28cd063c4a510fd00aec))
- feat: load algo config from yaml file by [@lexmiin](https://github.com/lexmiin) ([fdc922f](https://github.com/lexmiin/evocomp/commit/fdc922f12f52647b5b024e9fd0db5d1efda51bf8))
- feat: add `main.py` file by [@lexmiin](https://github.com/lexmiin) ([2a401e6](https://github.com/lexmiin/evocomp/commit/2a401e613c6ff50ed7caf98b86226c8d5aa22a67))
- fix: typo by [@lexmiin](https://github.com/lexmiin) ([36bd1c1](https://github.com/lexmiin/evocomp/commit/36bd1c12594cfaa0d54839b59c2bf880d812af03))
- feat: handle invalid cli inputs for algo and algo params by [@lexmiin](https://github.com/lexmiin) ([5fa4080](https://github.com/lexmiin/evocomp/commit/5fa408010df28659917335765fb2f74b0759bee7))
- refactor: improve typing by [@lexmiin](https://github.com/lexmiin) ([3f04fae](https://github.com/lexmiin/evocomp/commit/3f04fae693f7dea0e2f2d7145c40073194d3e16b))
- refactor: convert project into library by [@lexmiin](https://github.com/lexmiin) ([509a7bd](https://github.com/lexmiin/evocomp/commit/509a7bd67807c7f2cbe43c6395c35dc31e6e56f5))
- fix: incorrect return of epochs by [@lexmiin](https://github.com/lexmiin) ([ada3d30](https://github.com/lexmiin/evocomp/commit/ada3d30e6855755a3f23c33956c4c7dd9534d074))
- feat: do either maximization or minimization of objective by [@lexmiin](https://github.com/lexmiin) ([0533b42](https://github.com/lexmiin/evocomp/commit/0533b42fc6a0fe9338a83e9ac77970e880f50190))
- fix: export SymbioticOptimisation by [@lexmiin](https://github.com/lexmiin) ([19d7e48](https://github.com/lexmiin/evocomp/commit/19d7e48c25df37c1325d522c1072460cd71d198d))
- feat: tune methods to work on n-dimensional problems and maximization by [@lexmiin](https://github.com/lexmiin) ([909eeb9](https://github.com/lexmiin/evocomp/commit/909eeb981c2449b0f855e9f7c6ff32dfb6a8a140))
- refactor: limit simulated annealing to minimization by [@lexmiin](https://github.com/lexmiin) ([80197d3](https://github.com/lexmiin/evocomp/commit/80197d3c7ff26cf7ceba8eafb77d32631a5da757))
- refactor: `__create_mutant` and `__create_trial` methods by [@lexmiin](https://github.com/lexmiin) ([16a15bc](https://github.com/lexmiin/evocomp/commit/16a15bc630f45364476b19af0ad197c1427f8ac0))
- diff_evolution: clip mutant solution instead of mutant instance by [@lexmiin](https://github.com/lexmiin) ([e444e1b](https://github.com/lexmiin/evocomp/commit/e444e1bc119a75d4a1e5ccaa2efa3f5423bf0784))
- objective: align objective evaluate parameter name with base interface by [@lexmiin](https://github.com/lexmiin) ([748c74f](https://github.com/lexmiin/evocomp/commit/748c74f795d8ae0067946f5f6ac47cdd13f812bf))
- visualization: default display config as module singleton by [@lexmiin](https://github.com/lexmiin) ([009a8f5](https://github.com/lexmiin/evocomp/commit/009a8f5396b32d47fedba5c0ef71bd399c3fe364))
- python: manage project with uv by [@lexmiin](https://github.com/lexmiin) ([9730ece](https://github.com/lexmiin/evocomp/commit/9730ece1133bc0912221eeeb1cb1f86ec82fbe86))


### Documentation

- docs: update readme to include info about GP and parcels delivery by [@lexmiin](https://github.com/lexmiin) ([ff453c1](https://github.com/lexmiin/evocomp/commit/ff453c1d60e2455cad6e6e0ad6723f23fc78c3f5))
- docs: update heading levels by [@lexmiin](https://github.com/lexmiin) ([14479fb](https://github.com/lexmiin/evocomp/commit/14479fba76b6ca8ca5c73de9255cc0e4943e3bb1))
- docs: update README by [@lexmiin](https://github.com/lexmiin) ([68321ed](https://github.com/lexmiin/evocomp/commit/68321ed3acb34fea3b1b66638d219d455e94724c))
- docs: add toc by [@lexmiin](https://github.com/lexmiin) ([471b330](https://github.com/lexmiin/evocomp/commit/471b330f6d00cd5bdc2653a36902ea7fe1952e78))
- docs: update readme toc by [@lexmiin](https://github.com/lexmiin) ([aab908c](https://github.com/lexmiin/evocomp/commit/aab908c2905efd64f16092ab540469bb01bee849))
- docs: update readme by [@lexmiin](https://github.com/lexmiin) ([541bd50](https://github.com/lexmiin/evocomp/commit/541bd5001413749b9f0151659a43e1dc982655d8))
- docs: improve examples by [@lexmiin](https://github.com/lexmiin) ([0482bd6](https://github.com/lexmiin/evocomp/commit/0482bd66e138fa6f989a35b13a22652b2620c65c))
- docs: add docstrings for algorithms by [@lexmiin](https://github.com/lexmiin) ([6537852](https://github.com/lexmiin/evocomp/commit/65378521cf5c7a97f29755764dcaff179d803cf2))
- readme: update git url by [@lexmiin](https://github.com/lexmiin) ([c0cc9d8](https://github.com/lexmiin/evocomp/commit/c0cc9d83d9f90ba1bb39c1731038bb4c49e489b4))
- docs: update installation instructions by [@lexmiin](https://github.com/lexmiin) ([cf07757](https://github.com/lexmiin/evocomp/commit/cf077575e54c0278e16192893adcbfe8bc08af75))


### Internal

- chore(black): add black config by [@lexmiin](https://github.com/lexmiin) ([2ef0f99](https://github.com/lexmiin/evocomp/commit/2ef0f99c81f7461629a5cad04bb6e3de1ad38844))
- chore: update flake8 and black config by [@lexmiin](https://github.com/lexmiin) ([5af6aeb](https://github.com/lexmiin/evocomp/commit/5af6aeb721acda80293d027fac0061f1b96c0c3c))
- chore: ignore jupyter notebooks by [@lexmiin](https://github.com/lexmiin) ([62f5ac1](https://github.com/lexmiin/evocomp/commit/62f5ac11ef08e2b5a314d6ed9243d312cf72bc62))
- chore: add scipy to deps by [@lexmiin](https://github.com/lexmiin) ([64beba1](https://github.com/lexmiin/evocomp/commit/64beba1afa5c0a44476227bac7e7725728011853))
- chore: ignore notebooks dir by [@lexmiin](https://github.com/lexmiin) ([f2732cd](https://github.com/lexmiin/evocomp/commit/f2732cd4026f1ac678eea5ef26ca2512f0d690bf))
- chore: update isort config by [@lexmiin](https://github.com/lexmiin) ([3336908](https://github.com/lexmiin/evocomp/commit/33369081cda3bd10e53b9c4433fb14c970aa52be))
- chore: clean up by [@lexmiin](https://github.com/lexmiin) ([db53351](https://github.com/lexmiin/evocomp/commit/db53351fd652e52712991a2cceb42ac76e415347))
- chore: switch to ruff by [@lexmiin](https://github.com/lexmiin) ([6419cd7](https://github.com/lexmiin/evocomp/commit/6419cd722afa613629cfe81a5b1a295509f690fb))
- chore: update ruff config and run linter with fixes by [@lexmiin](https://github.com/lexmiin) ([53aa445](https://github.com/lexmiin/evocomp/commit/53aa44536f74d8e3b0f3c552b2f6da4efd20f439))
- chore: add flake by [@lexmiin](https://github.com/lexmiin) ([9d1fd9a](https://github.com/lexmiin/evocomp/commit/9d1fd9af4ca0d36d96d58dfd71b1a4b8a7599c24))
- chore: fix packaging by [@lexmiin](https://github.com/lexmiin) ([9c029fe](https://github.com/lexmiin/evocomp/commit/9c029fe2b1d6362955cfaa711e4a54cd991a9819))
- chore: fix dependencies issues by [@lexmiin](https://github.com/lexmiin) ([cae81cc](https://github.com/lexmiin/evocomp/commit/cae81cc8b3bd1970436cf4635aed742f7e582d5d))
- chore: remove `out` dir by [@lexmiin](https://github.com/lexmiin) ([534b8e6](https://github.com/lexmiin/evocomp/commit/534b8e6d659f2c723730c31452de715bd095e105))
- chore: type in author name by [@lexmiin](https://github.com/lexmiin) ([6ffe1fb](https://github.com/lexmiin/evocomp/commit/6ffe1fb999a80241b8cf63d8279f3c74c1775601))
- chore: add license by [@lexmiin](https://github.com/lexmiin) ([1c82c8a](https://github.com/lexmiin/evocomp/commit/1c82c8ada4ba2db8124d3e870bfe76cd2143f42f))
- chore: lint fixes and formatting by [@lexmiin](https://github.com/lexmiin) ([9ca1464](https://github.com/lexmiin/evocomp/commit/9ca1464956adbd5b73f51364c5a687cff6b860a1))
- ci: release workflow by [@lexmiin](https://github.com/lexmiin) ([d0dd636](https://github.com/lexmiin/evocomp/commit/d0dd6361a74eb69fffab809b5bca92b653049f51))


### New contributors

- @lexmiin made their first contribution in [#2](https://github.com/lexmiin/evocomp/pull/2)

<!-- generated by git-cliff -->
