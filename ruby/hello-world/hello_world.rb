class HelloWorld

  def self.hello(name=nil)
    if name != nil
      return "Hello, #{name}!"
    else
      return "Hello, World!"
    end
  end

end