![](https://github.com/artdgn/pages/workflows/CI/badge.svg) 
![](https://github.com/artdgn/pages/workflows/GH-Pages%20Status/badge.svg) 

-----------

#### View at:
# https://artdgn.github.io/pages

-----------
![](https://artdgn.github.io/images/covid-pages.gif)
### Automatically updating notebook posts, mainly for COVID-19 data related questions I couldn't find answers to in other places.

- Most of the [fastpages](https://github.com/fastai/fastpages) / github-actions automation and a lot of the initial data prep 
code for COVID-19 JHU data is taken from [covid19dashboards.com ](https://github.com/github/covid19-dashboard) project.
- Dashboards from this repo that are merged in [covid19dashboards.com ](https://github.com/github/covid19-dashboard):
  - [World News from data](https://covid19dashboards.com/covid-news/)
  - [ICU projections](https://covid19dashboards.com/covid-progress-projections/)
    

-----------

### Local development:
- Install in .venv: `make install`
- Update / create local notebooks from `.py` files: `make notebooks` 
- Run jupyter notebook server: `make jupyter` 
- Run jekyll (the blog server): `make server`