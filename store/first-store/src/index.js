import React, { Component } from 'react'

export default class Store extends Component {
  constructor() {
    super();
  }
  render() {
    return (
      <div>Store</div>
    )
  }


  
  buildStore() {
    let formStore = new FormStore();
  
    formStore.append("armor_item", this.state.armor);
    formStore.append("weapons_item", this.state.weapons);
    formStore.append("items_item", this.state.items);
  
  
    return formStore;
  }
}

