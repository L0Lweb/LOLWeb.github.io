# see: curl -s https://pages.github.com/versions.json | jq -r '.ruby'
FROM ruby:3.3.4

WORKDIR /LOLWeb/

COPY ./Gemfile ./Gemfile.lock ./

RUN bundle install

ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host=0.0.0.0"]
