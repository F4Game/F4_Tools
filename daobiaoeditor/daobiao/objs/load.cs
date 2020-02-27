//导表开始

using System.Collections;
using System.Collections.Generic;

public class PersonFactory
{
    private Dictionary<int,Person> personDict = new Dictionary<int, Person>();
    
    public PersonFactory()
    {
		this.personDict.Add(1, new Person1());
		this.personDict.Add(2, new Person2());
		this.personDict.Add(3, new Person3());
		this.personDict.Add(4, new Person4());
		this.personDict.Add(5, new Person5());
		this.personDict.Add(6, new Person6());

    }

    public Person CreatePerson(int personId)
    {
        return this.personDict[personId].Clone();
    }
}
        
//导表结束
