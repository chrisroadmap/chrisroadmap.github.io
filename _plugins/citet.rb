# Narrative citation tag for jekyll-scholar: {% citet key %} renders
# "Author et al. (2026)" instead of the parenthetical "(Author et al., 2026)".
# It reuses {% cite %}, so the link to the bibliography entry is kept.
# Single keys only: a multi-key group such as "(A, 2020; B, 2021)" is not rewritten.
module Jekyll
  class Scholar
    class CiteTTag < CiteTag
      def render(context)
        super.sub(/\((.+?), (\d{4}[a-z]?)\)/, '\1 (\2)')
      end
    end
  end
end

Liquid::Template.register_tag('citet', Jekyll::Scholar::CiteTTag)
