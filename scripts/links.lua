function Link(elem)
  local target = elem.target
  -- Only transform relative .md links, not URLs
  if not target:match('^[a-zA-Z]+://')
     and not target:match('^/') then
    -- Replace .md (with optional anchor/query) with .html
    elem.target = target
      :gsub('%.md([#?].*)', '.html%1')
      :gsub('%.md$', '.html')
  end
  return elem
end