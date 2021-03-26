const Prod = require('../models/prod');


exports.get_test = (req,res,next) => {


    res.render('admin/add_product', {
        pageTitle: 'Add Product',
        path: '/admin/add-product',
        editing: false
    });


};

exports.post_test = (req,res,next) => {
    const title = req.body.title;
    const image = req.body.image;
    const price = req.body.price;
    const quantity = req.body.quantity;
    const product = new Prod( title, image, price,quantity);
    product
        .add_prod()
        .then(() => {
            res.redirect('/admin/add-product');
        })
        .catch(err => console.log(err));
};


exports.get_prods_test = (req,res,next) => {

    const a = Prod.get_all();
    a.then(value => {res.render('prods', {pageTitle: 'Products', path: '/prods', editing: false, articles:value.rows});});

   

};

exports.post_prods_test = (req,res,next) => {
    //    .catch(err => console.log(err));
};




exports.get_cart_test = (req,res,next) => {

    const a = Prod.get_all_cart();
    var x;
    const b = Prod.get_credit();
   
    a.then(value => {x = value; return Prod.get_credit();})
    .then(val => {res.render('cart', {pageTitle: 'Cart', path: '/cart', editing: false, articles:x.rows, count: x.rowCount, cred: val.rows[0].credit });});
   

};

exports.post_cart_test = (req,res,next) => {
   
    const product_id = req.body.product_id;

   
    const nice = Prod.get_with_prod_id(product_id);
    nice.then(val => {if(val.rowCount != 0) 
        {return Prod.get_in_cart_id(product_id).then(value => {Prod.update_in_prod(product_id); if(value.rowCount != 0) {return Prod.update_in_cart(product_id)} else return Prod.insert_in_cart(product_id)})
    .then(() => {return res.redirect('/cart')}); } 
    else {return res.redirect('/prods')}});
   
};



exports.get_orders_test = (req,res,next) => {

    const ord = Prod.get_all_orders();
    ord.then(value => {res.render('orders', {pageTitle: 'Orders', path: '/orders', editing: false, articles:value.rows});});

   

};

exports.post_orders_test = (req,res,next) => {
   
    const cred = Prod.remcred();
    var x,y;
    var pur;
    var pro_list = [];
    var res_list = [];
    var id_list = [];
    var newlist = [];

    cred.then(val => { x = val.rows[0].credit; return Prod.sum_price_cart()})
        .then(value => {if(x < value.rows[0].sum) {return res.redirect('/cart') } 
        else {pur = value.rows[0].sum; return Prod.get_full_cart().then(ui => {y = ui.rowCount;
            //  console.log(y);
          for (i = 0; i < y; i++) {
          var id = ui.rows[i].item_id;
          id_list.push(id);
          pro_list.push(Prod.present_in_orders(id))} return Promise.all(pro_list)} )
          .then(chec => {
              for (i = 0; i < chec.length; i++) {
                  
                  if(chec[i].rowCount == 0)
                  {//   console.log("id"+id_list[i]);
                      newlist.push(Prod.insert_order(id_list[i]));
                  }
                  else
                  {  // console.log("id"+id_list[i]);
                      newlist.push(Prod.update_order(id_list[i]));
                  }
              }

              return Promise.all(newlist);

          })
          .then(()=>{return Prod.empty_cart()})
          .then(() => {return Prod.update_credit(pur)})
          .then(()=>{res.redirect('/orders')});}})    
            
            
             
          
           
};


