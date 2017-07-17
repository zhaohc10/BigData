# Usage

# Creation of virtualenv:

virtualenv -p python3 <desired-path>
# Activate the virtualenv:

source <desired-path>/bin/activate
# Deactivate the virtualenv:

deactivate




# __call__

# 在Python中，函数其实是一个对象：

# >>> f = abs
# >>> f.__name__
# 'abs'
# >>> f(-123)
# 123
# 由于 f 可以被调用，所以，f 被称为可调用对象。

# 所有的函数都是可调用对象。

# 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。



def timeit_3_for_wraps(func):
    @functools.wraps(func)
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print 'used:',end-start
    return wrapper

# @timeit_3_for_wraps
# def foo6():
#     print 'this is foo6'
# foo6()



# 你写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他使用者就能清楚的知道这个函数应该怎么使用。

# 解决方案
# 使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数。 例如，下面有一个被注解了的函数：

# def add(x:int, y:int) -> int:
#     return x + y
# python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。 
# 然而，对于那些阅读源码的人来讲就很有帮助啦。第三方工具和框架可能会对这些注解添加语义。同时它们也会出现在文档中。

# >>> help(add)
# Help on function add in module __main__:
# add(x: int, y: int) -> int
# >>>


#********************************************************************************************************************************************************************
# 						http://www.jianshu.com/p/9771b0a3e589
#********************************************************************************************************************************************************************
# >>> from sqlalchemy import ForeignKey
# >>> from sqlalchemy.orm import relationship

# >>> class Address(Base):
# ...     __tablename__ = 'addresses'
# ...     id = Column(Integer, primary_key=True)
# ...     email_address = Column(String, nullable=False)
# ...     user_id = Column(Integer, ForeignKey('users.id'))
# ...
# ...     user = relationship("User", back_populates="addresses")
# ...
# ...     def __repr__(self):
# ...         return "<Address(email_address='%s')>" % self.email_address

# >>> User.addresses = relationship(
# ...     "Address", order_by=Address.id, back_populates="user")


# 上面的代码中我们使用了一个新的名为ForeignKey的构造。其含义为，
# 其所在的列的值域应当被限制在另一个表的指定列的取值范围之类。这一特性是关系型数据库的核心特性之一。
# 就上例而言，addresses.user_id这一列的取值范围，应当包含在users.id的取值范围之内。

# 除了ForeignKey之外，我们还引入了一个relationship，来告诉ORM，Address类需要被连接到User类。
# relationship和ForeignKey这个两个属性决定了表之间关系的属性，决定了这个关系是多对一的。

# 在完成对Address类的声明之后，我们还定义另一个relationship，将其赋值给了User.addresses。
# 在两个relationship中，我们都有传入了一个relationship.back_populates的属性来为反向关系所对应的属性进行命名。


# 现在，当我们创建一个User实例的时候，会同时创建一个空的addresses的collection。
# 这个collection可能是多种类型，如list, set, 或是dictionary。默认情况下，其应当为一个Python列表。

# >>> jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
# >>> jack.addresses
# []

#********************************************************************************************************************************************************************
#. scala sbt. http://twitter.github.io/scala_school/zh_cn/sbt.html
#********************************************************************************************************************************************************************
sbt执行步骤：
sbt 完全按照约定工作。sbt 将会自动找到以下内容：

项目根目录下的源文件
src/main/scala 或 src/main/java 中的源文件
src/test/scala 或 src/test/java 中的测试文件
src/main/resources 或 src/test/resources 中的数据文件
lib 中的 jar 文件
#———————————————————————————————————————————————————————————————————————
# The trick is to figure out which lib directory to put your JAR in. 
# You can do this by running the following in your sbt console: show unmanagedBase
#———————————————————————————————————————————————————————————————————————
批处理模式 
你也可以用批处理模式来运行 sbt，可以以空格为分隔符指定参数。对于接受参数的 sbt 命令，将命令和参数用引号引起来一起传给 sbt。例如：
$ sbt clean compile "testOnly TestA TestB"

# clean	删除所有生成的文件 （在 target 目录下）。
# compile	编译源文件（在 src/main/scala 和 src/main/java 目录下）。
# test	编译和运行所有测试。
# console	进入到一个包含所有编译的文件和所有依赖的 classpath 的 Scala 解析器。输入 :quit， Ctrl+D （Unix），或者 Ctrl+Z （Windows） 返回到 sbt。
# run <参数>*	在和 sbt 所处的同一个虚拟机上执行项目的 main class。
# package	将 src/main/resources 下的文件和 src/main/scala 以及 src/main/java 中编译出来的 class 文件打包成一个 jar 文件。
# help <命令>	显示指定的命令的详细帮助信息。如果没有指定命令，会显示所有命令的简介。
# reload	重新加载构建定义（build.sbt， project/*.scala， project/*.sbt 这些文件中定义的内容)。在修改了构建定义文件之后需要重新加载。

# actions – 显示对当前工程可用的命令
# update – 下载依赖
# publish-local – 把构建出来的jar包安装到本地的ivy缓存
# publish – 把jar包发布到远程仓库（如果配置了的话)
# assembly- 只使用sbt的 package 命令打包，是不会把这些第三方库打包进去的。
# 			所以，这个时候我们就需要sbt的assembly pulgin。它的任务，就是负责把所有依赖的jar包都打成一个 fat jar。


#spark的依赖直接忽略, 使用关键词provided表示运行环境已经有，不需要打包
libraryDependencies += "org.apache.spark" %% "spark-core" % "1.5.2" % "provided"

#依赖spark-cassandra-connector的库
libraryDependencies += "com.datastax.spark" %% "spark-cassandra-connector" % "1.5.0-M2"

#如果后缀是.properties的文件，合并策略采用（MergeStrategy.first）第一个出现的文件
assemblyMergeStrategy in assembly := {
  case PathList(ps @ _*) if ps.last endsWith ".properties" => MergeStrategy.first
  case x =>
    val oldStrategy = (assemblyMergeStrategy in assembly).value
    oldStrategy(x)
}

# project目录即相关文件介绍
# project目录下的几个文件实际上都是非必须存在的，可以根据情况添加。
# build.properties 文件声明使用的要使用哪个版本的SBT来编译当前项目， 
build文件的类型（是*.sbt还是*.scala）；
build文件的存放位置（*.sbt文件只有存放在项目的根目录下， SBT才会关注它或者它们， 
而*.scala文件只有存放在项目根目录下的project目录下，SBT才不会无视它或者它们
#********************************************************************************************************************************************************************
#. mvn  useful command line -->  http://www.trinea.cn/android/maven/     https://my.oschina.net/zhanghaiyang/blog/725803  http://www.cnblogs.com/boshen-hzb/p/6553064.html
#********************************************************************************************************************************************************************
Maven本质上是一个插件框架，它的核心并不执行任何具体的构建任务，所有这些任务都交给插件来完成，例如编译源代码是由maven-compiler-plugin完成的。

进一步说，每个任务对应了一个插件目标（goal），每个插件会有一个或者多个目标，例如
maven-compiler-plugin的compile目标用来编译位于src/main/java/目录下的主源码，
testCompile目标用来编译位于src/test/java/目录下的测试源码。

maven-archetype-plugin： Archtype指项目的骨架，Maven初学者最开始执行的Maven命令可能就是mvn archetype:generate，这实际上就是让maven-archetype-plugin生成一个很简单的项目骨架，帮助开发者快速上手。
maven-assembly-plugin：  的用途是制作项目分发包，该分发包可能包含了项目的可执行文件、源代码、readme、平台脚本等等。
maven-compiler-plugin：  为了使项目结构更为清晰，Maven区别对待Java代码文件和资源文件，maven-compiler-plugin用来编译Java代码，
maven-resources-plugin： maven-resources-plugin则用来处理资源文件,默认的主资源文件目录是src/main/resources。
maven-javadoc-plugin：   源码包和Javadoc包就是附属构件的极佳例子
maven-shade-plugin：     可以让用户配置Main-Class的值，然后在打包的时候将值填入/META-INF/MANIFEST.MF文件  
maven-dependency-plugin： 最大的用途是帮助分析项目依赖，list能够列出项目最终解析到的依赖列表。tree能进一步的描绘项目依赖树。
maven-release-plugin：   帮助自动化项目版本发布，它依赖于POM中的SCM信息，prepare用来准备版本发布，具体的工作包括检查是否有未提交代码、检查是否有SNAPSHOT依赖、

-D 传入属性参数 


mvn -version/-v                                                   显示版本信息 
mvn archetype:create -DgroupId=com.oreilly -DartifactId=my-app    创建mvn项目 
mvn package                                                       生成target目录，编译、测试代码，生成测试报告，生成jar/war文件
mvn -Dtest package                                                只打包不测试
mvn jetty:run                                                     运行项目于jetty上, 
mvn compile                                                       编译 
mvn test                                                          编译并测试 
mvn clean                                                         清空生成的文件 
mvn site                                                          生成项目相关信息的网站 
mvn -Dwtpversion=1.0 eclipse:eclipse                              生成Wtp插件的Web项目 
mvn -Dwtpversion=1.0 eclipse:clean                                清除Eclipse项目的配置信息(Web项目) 
mvn eclipse:eclipse                                               将项目转化为Eclipse项目

mvn exec:java -Dexec.mainClass=org.sonatype.mavenbook.weather.Main Exec 插件让我们能够在不往 classpath 载入适当的依赖的情况下，运行这个程序 
mvn dependency:resolve 打印出已解决依赖的列表 
mvn dependency:tree 打印整个依赖树 





pom是指project object Model。pom是一个xml,pom文件中包含了项目的信息和maven build项目所需的配置信息，通常有项目信息(如版本、成员)、项目的依赖、插件和goal、build选项等等
pom是可以继承的，通常对于一个大型的项目或是多个module的情况，子模块的pom需要指定父模块的pom



# maven pom.xml中的 build说明

defaultGoal，执行构建时默认的goal或phase，如jar:jar或者package等
directory，构建的结果所在的路径，默认为${basedir}/target目录
finalName，构建的最终结果的名字，该名字可能在其他plugin中被改变

<resources>   资源往往不是代码，无需编译，而是一些properties或XML配置文件，构建过程中会往往会将资源文件从源路径复制到指定的目标路径。
<plugins>     给出构建过程中所用到的插件。


# maven pom.xml中的 dependencies说明

project         pom文件的顶级元素
modelVersion    所使用的object model版本，为了确保稳定的使用，这个元素是强制性的。除非maven开发者升级模板，否则不需要修改
groupId         是项目创建团体或组织的唯一标志符，通常是域名倒写，如groupId  org.apache.maven.plugins就是为所有maven插件预留的
artifactId      是项目artifact唯一的基地址名
packaging       artifact打包的方式，如jar、war、ear等等。默认为jar。这个不仅表示项目最终产生何种后缀的文件，也表示build过程使用什么样的lifecycle。
version         artifact的版本，通常能看见为类似0.0.1-SNAPSHOT，其中SNAPSHOT表示项目开发中，为开发版本
name            表示项目的展现名，在maven生成的文档中使用
url             表示项目的地址，在maven生成的文档中使用
description     表示项目的描述，在maven生成的文档中使用
dependencies    表示依赖，在子节点dependencies中添加具体依赖的groupId artifactId和version
build           表示build配置
parent          表示父pom




validate          验证项目是否正确以及必须的信息是否可用
compile           编译源代码
test              测试编译后的代码，即执行单元测试代码
package           打包编译后的代码，在target目录下生成package文件
integration-test  处理package以便需要时可以部署到集成测试环境
verify            检验package是否有效并且达到质量标准
install           安装package到本地仓库，方便本地其它项目使用
deploy            部署，拷贝最终的package到远程仓库和替他开发这或项目共享，在集成或发布环境完成

#********************************************************************************************************************************************************************
pylint keyword 
  # There are 5 kind of message types :
  # * (C) convention, for programming standard violation
  # * (R) refactor, for bad code smell
  # * (W) warning, for python specific problems
  # * (E) error, for much probably bugs in the code
  # * (F) fatal, if an error occurred which prevented pylint from doing further processing.
#********************************************************************************************************************************************************************

# netstat -lntu

	# -l = only services which are listening on some port
	# -n = show port number, don't try to resolve the service name
	# -t = tcp ports
	# -u = udp ports
	# -p = name of the program

#********************************************************************************************************************************************************************

# 最基本的格式是 CSV ，其廉价并且不需要顶一个一个 schema 和数据关联。

# 随后流行起来的一个通用的格式是 XML，其有一个 schema 和 数据关联，XML 广泛的使用于 Web Services 和 SOA 架构中。不幸的是，其非常冗长，并且解析 XML 需要消耗内存。

# 另外一种格式是 JSON，其非常流行易于使用因为它非常方便易于理解。
# 这些格式在 Big Data 环境中都是不可拆分的，这使得他们难于使用。在他们之上使用一个压缩机制（Snappy，Gzip）并不能解决这个问题。

# 因此不同的数据格式出现了。Avro 作为一种序列化平台被广泛使用，因为它能跨语言，提供了一个小巧紧凑的快速的二进制格式，
# 支持动态 schema 发现（通过它的泛型）和 schema 演变，并且是可压缩和拆分的。它还提供了复杂的数据结构，例如嵌套类型。


# Avro设计之初就用来支持数据密集型应用，适合于远程或本地大规模数据的存储和交换。它的主要特点有：
# 	丰富的数据结构类型；
# 	快速可压缩的二进制数据形式，对数据二进制序列化后可以节约数据存储空间和网络传输带宽；
# 	存储持久数据的文件容器；
# 	可以实现远程过程调用RPC；
# 	简单的动态语言结合功能。

Avro依赖模式(Schema)来实现数据结构定义。可以把模式理解为Java的类，它定义每个实例的结构，可以包含哪些属性。可以根据类来产生任意多个实例对象。

Avro支持两种序列化编码方式：二进制编码和JSON编码。使用二进制编码会高效序列化，并且序列化后得到的结果会比较小；而JSON一般用于调试系统或是基于WEB的应用。
对Avro数据序列化/反序列化时都需要对模式以深度优先(Depth-First)，从左到右(Left-to-Right)的遍历顺序来执行。

Avro为了便于MapReduce的处理定义了一种容器文件格式(Container File Format)。这样的文件中只能有一种模式，所有需要存入这个文件的对象都需要按照这种模式以二进制编码的形式写入。
对象在文件中以块(Block)来组织，并且这些对象都是可以被压缩的。块和块之间会存在同步标记符(Synchronization Marker)，以便MapReduce方便地切割文件用于处理


#*******************
# how check the port
macbook : netstat -ap tcp
linuxt : netstat -nltp 

# *******************
kafka--
listeners is what the broker will use to create server sockets.
advertised.listeners is what clients will use to connect to the brokers.


#************
public class GenericTest {

    public static void main(String[] args) {
        /*
        List list = new ArrayList();
        list.add("qqyumidi");
        list.add("corn");
        list.add(100);
        */

        List<String> list = new ArrayList<String>();
        list.add("qqyumidi");
        list.add("corn");
        //list.add(100);   // 1  提示编译错误

        for (int i = 0; i < list.size(); i++) {
            String name = list.get(i); // 2
            System.out.println("name:" + name);
        }
    }
}

# 在//1处想加入一个Integer类型的对象时会出现编译错误，通过List<String>，直接限定了list集合中只能含有String类型的元素，
# 在//2处无须进行强制类型转换，因为此时，集合能够记住元素的类型信息，编译器已经能够确认它是String类型了
# 我们知道在List<String>中，String是类型实参，也就是说，相应的List接口中肯定含有类型形参。且get()方法的返回结果也直接是此形参类型（也就是对应的传入的类型实参）



惰性变量只能是不可变变量，并且只有在调用惰性变量时，才会去实例化这个变量。



#********************

VBoxManage modifyvm zhc --memory 3000


